from django.db.models import Q
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse as json_resp
from django_filters.rest_framework import DjangoFilterBackend
from product import models as product_models
from product.api import serializers as product_ser


class ChangeStateAndMoveView(APIView):
    def put(self, request, pk, *args, **kwargs):
        try:
            # Получаем состояние из запроса
            new_state = request.data.get('state')

            if new_state == 'defect':
                # Получаем объект из ProductNormal
                product_normal = product_models.ProductNormal.objects.get(pk=pk)
                # Создаем новый объект в ProductDefect
                product_defect_serializer = product_ser.ProductDefectSerializer(data={
                    'name': product_normal.name,
                    'category': request.data.get('category'),
                    'identification_number': product_normal.identification_number,
                    'unit': product_normal.unit,
                    'quantity': product_normal.quantity,
                    'price': product_normal.price,
                    'sum': product_normal.sum,
                    'state': new_state,
                })

                if product_defect_serializer.is_valid():
                    product_defect_serializer.save()
                else:
                    return Response(product_defect_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                # Удаляем объект из ProductNormal
                product_normal.delete()

                return Response(product_defect_serializer.data, status=status.HTTP_200_OK)

            elif new_state == 'normal':
                # Получаем объект из ProductDefect
                product_defect = product_models.ProductDefect.objects.get(pk=pk)
                # Создаем новый объект в ProductNormal
                product_normal_serializer = product_ser.ProductNormalSerializer(data={
                    'name': product_defect.name,
                    'category': request.data.get('category'),
                    'identification_number': product_defect.identification_number,
                    'unit': product_defect.unit,
                    'quantity': product_defect.quantity,
                    'price': product_defect.price,
                    'sum': product_defect.sum,
                    'state': new_state,
                })

                if product_normal_serializer.is_valid():
                    product_normal_serializer.save()
                else:
                    return Response(product_normal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                # Удаляем объект из ProductDefect
                product_defect.delete()

                return Response(product_normal_serializer.data, status=status.HTTP_200_OK)

            # Если состояние не "defect" или "normal", возвращаем ошибку
            return Response({'detail': 'Invalid state.'}, status=status.HTTP_400_BAD_REQUEST)

        except product_models.ProductNormal.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)



class ProducDefecttItemViewSet(ModelViewSet):
    serializer_class = product_ser.ProductDefectItemSerializer
    lookup_field = 'pk'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'identification_number']

    def get_queryset(self):
        queryset = product_models.ProductDefect.objects.filter(is_archived=False)

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
        instance.is_archived = True
        instance.save()

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
        queryset = product_models.ProductNormal.objects.filter(is_archived=False)

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
        instance.is_archived = True
        instance.save()

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
        instance.is_archived = False
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class Search(APIView):
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name']

    def get(self, request, format=None):
        queryset = product_models.ProductNormal.objects.filter(is_archived=False)

        search_query = request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(name__iregex=fr'.*{search_query}.*')
            )

        # Получаем уникальные имена и категории
        unique_names_and_categories = queryset.values_list('name', 'category').distinct()

        # Создаем список словарей с уникальными именами и категориями
        result_data = [{'name': name, 'category': category} for name, category in unique_names_and_categories]

        serializer = product_ser.SearchSer(result_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)