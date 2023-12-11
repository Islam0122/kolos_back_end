from django.db import transaction
from django.db.models import Q
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product import models as product_models
from product.api import serializers as product_ser
from product.models import ProductNormal, ProductDefect, Warehouse
from django.shortcuts import get_object_or_404
from product.choices import State
from rest_framework.views import APIView
import pdb


class MoveNormalToDefectiveAPIView(APIView):
    def post(self, request, pk, *args, **kwargs):

        try:
            normal_product = get_object_or_404(ProductNormal, pk=pk)
            new_warehouse = get_object_or_404(Warehouse, pk=2)

            with transaction.atomic():
                # Проверяем, существует ли товар с таким же identification_number в браке
                existing_defective_product = ProductDefect.objects.filter(
                    product__identification_number=normal_product.identification_number,
                    warehouse=new_warehouse, quantity__gt=0
                ).first()

                if existing_defective_product:
                    # Товар уже существует в браке, увеличиваем количество
                    existing_defective_product.quantity += normal_product.quantity
                    existing_defective_product.save()
                else:
                    # Создаем новый товар в браке
                    defective_product = ProductDefect.objects.create(
                        product=normal_product,
                        quantity=normal_product.quantity,
                        warehouse=new_warehouse,
                    )

                # Изменяем состояние нормального товара на "defect"
                normal_product.state = State.DEFECT
                normal_product.quantity = 0
                normal_product.save()

            return Response({"detail": "Товар успешно перемещен из нормы в брак"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": f"Ошибка при перемещении товара: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MoveDefectiveToNormalAPIView(APIView):
    def post(self, request, pk, *args, **kwargs):

        try:
            defective_product = get_object_or_404(ProductDefect, pk=pk)
            new_warehouse = get_object_or_404(Warehouse, pk=1)

            with transaction.atomic():
                # Проверяем, существует ли товар с таким же identification_number на новом складе
                existing_normal_product = ProductNormal.objects.filter(
                    identification_number=defective_product.product.identification_number,
                    warehouse=new_warehouse,
                ).first()

                if existing_normal_product:
                    # Устанавливаем состояние NORMAL для существующего нормального товара
                    existing_normal_product.state = State.NORMAL
                    existing_normal_product.save()

                    # Товар уже существует на новом складе, увеличиваем количество
                    existing_normal_product.quantity += defective_product.quantity
                    existing_normal_product.save()
                else:
                    # Создаем новый товар на новом складе
                    normal_product = ProductNormal.objects.create(
                        name=defective_product.product.name,
                        category=defective_product.product.category,
                        identification_number=defective_product.product.identification_number,
                        unit=defective_product.product.unit,
                        quantity=defective_product.quantity,
                        price=defective_product.product.price,
                        state=State.NORMAL,
                        warehouse=new_warehouse,
                    )

                # Удаляем запись из брака
                defective_product.delete()

            return Response({"detail": "Товар успешно перемещен из брака в норму"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": f"Ошибка при перемещении товара: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductDefectItemViewSet(ModelViewSet):
    serializer_class = product_ser.ProductDefectItemSerializer
    lookup_field = 'pk'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['product__name', 'product__identification_number']

    def get_queryset(self):
        queryset = product_models.ProductDefect.objects.select_related('product__category').filter(is_archived=False, quantity__gt=0)
        # Фильтрация по комбинированным полям без учета регистра и акцентов (для PostgreSQL)
        search_query = self.request.query_params.get('search_query', None)
        if search_query:
            queryset = queryset.filter(
                Q(product__name__iregex=fr'.*{search_query}.*') |
                Q(product__identification_number__iregex=fr'.*{search_query}.*')
            )

        category_filter = self.request.query_params.get('category', None)
        if category_filter:
            queryset = queryset.filter(product__category__title__iexact=category_filter)

        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # instance.is_archived = True
        instance.archived()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class ProductItemViewSet(ModelViewSet):
    serializer_class = product_ser.ProductItemSerializer
    lookup_field = 'pk'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'identification_number']

    def get_queryset(self):
        queryset = product_models.ProductNormal.objects.filter(is_archived=False, state='normal').order_by('-id')
        # Фильтрация по комбинированным полям без учета регистра и акцентов (для PostgreSQL)
        search_query = self.request.query_params.get('search_query', None)
        if search_query:
            queryset = queryset.filter(
                Q(name__iregex=fr'.*{search_query}.*') |
                Q(identification_number__iregex=fr'.*{search_query}.*')
            )

        # Фильтрация по отдельным полям без учета регистра (для PostgreSQL)
        state_filter = self.request.query_params.get('state', None)
        if state_filter:
            queryset = queryset.filter(state__iexact=state_filter)

        category_filter = self.request.query_params.get('category', None)
        if category_filter:
            queryset = queryset.filter(category__title__iexact=category_filter)

        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # instance.is_archived = True
        instance.archived()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




class ArchivedProductView(ModelViewSet):
    queryset = product_models.ProductNormal.objects.filter(is_archived=True)
    serializer_class = product_ser.ProductItemSerializer
    lookup_field = 'pk'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'identification_number']

    # restore -> product
    def restore(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.restore()

        return Response(status=status.HTTP_200_OK)

class ArchivedDefectProductView(ModelViewSet):
    queryset = product_models.ProductDefect.objects.filter(is_archived=True)
    serializer_class = product_ser.ProductDefectItemSerializer

    lookup_field = 'pk'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'identification_number']

    # restore -> product
    def restore(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.restore()

        return Response(status=status.HTTP_200_OK)

class CombinedProductView(APIView):
    def get(self, request, *args, **kwargs):
        normal_products = ProductNormal.objects.filter(is_archived=True)
        defect_products = ProductDefect.objects.filter(is_archived=True)

        normal_serializer = product_ser.ProductNormalSerializer(normal_products, many=True)
        defect_serializer = product_ser.ProductDefectItemSerializer(defect_products, many=True)

        combined_products = normal_serializer.data + defect_serializer.data

        return Response(combined_products)

class Search(APIView):
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name']

    def get(self, request, format=None):
        queryset = product_models.ProductNormal.objects.filter(is_archived=False).select_related('category')

        search_query = request.query_params.get('search_query', None)
        if search_query:
            queryset = queryset.filter(
                Q(name__iregex=fr'.*{search_query}.*')
            )

        category_filter = self.request.query_params.get('category', None)
        if category_filter:
            queryset = queryset.filter(category__title__iexact=category_filter)

        # Получаем уникальные имена и категории
        unique_names_and_categories = queryset.values_list('name', 'category').distinct()

        # Создаем список словарей с уникальными именами и категориями
        result_data = [{'name': name, 'category': category} for name, category in unique_names_and_categories]

        serializer = product_ser.SearchSer(result_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SearchDefect(ModelViewSet):
    serializer_class = product_ser.SearchDefectSerializer
    lookup_field = 'pk'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['product__name', 'product__identification_number']

    def get_queryset(self):
        queryset = product_models.ProductDefect.objects.filter(is_archived=False).select_related('product__category').filter( quantity__gt=0)
        # Фильтрация по комбинированным полям без учета регистра и акцентов (для PostgreSQL)
        search_query = self.request.query_params.get('search_query', None)
        if search_query:
            queryset = queryset.filter(
                Q(product__name__iregex=fr'.*{search_query}.*') |
                Q(product__identification_number__iregex=fr'.*{search_query}.*')
            )

        category_filter = self.request.query_params.get('category', None)
        if category_filter:
            queryset = queryset.filter(product__category__title__iexact=category_filter)

        # return queryset
        print(queryset)
        # Получаем уникальные имена и категории
        unique_names_and_categories = queryset.values_list('product__name', 'product__category').distinct()
        print(unique_names_and_categories)

        # Создаем список словарей с уникальными именами и категориями
        result_data = [{'name': name, 'category': category} for name, category in unique_names_and_categories]

        serializer = product_ser.SearchDefectSerializer(result_data, many=True)
        # breakpoint()
        return serializer.data

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # instance.is_archived = True
        instance.archived()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class CategoryListAPIView(ListAPIView):
    queryset = product_models.Category.objects.all()
    serializer_class = product_ser.CategorySerializer