from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# from apps.core.filters import ProductFilter
from .models import Product
from .serializer import ProductSerializers
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(ModelViewSet):  # GET/PUT/DELETE/CREATE/
    queryset = Product.objects.filter(is_archived=False).select_related('category')
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'


class ArchivedProductView(ModelViewSet):
    queryset = Product.objects.filter(is_archived=True).select_related('category')
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'

# filter_backends = (DjangoFilterBackend,)
# filterset_class = ProductFilter

# def destroy(self, request, *args, **kwargs):
#     instance = self.get_object()
#
#     archive_product = ArchiveProduct(
#         title=instance.title,
#         category=instance.category,
#         identification_number=instance.identification_number,
#         unit_of_measurement=instance.unit_of_measurement,
#         quantity=instance.quantity,
#         price=instance.price,
#         status=instance.status,
#
#     )
#     archive_product.save()
#     instance.delete()
#
#     return Response(status=status.HTTP_204_NO_CONTENT)


# class ArchivedProductView(ModelViewSet):
#     queryset = ArchiveProduct.objects.all()
#     serializer_class = ArchivedProductSerializer
#     lookup_field = 'pk'
#
#     def restore(self, request, pk):
#         archive_product = ArchiveProduct.objects.get(pk=pk)
#         new_product = Product(
#             title=archive_product.title,
#             category=archive_product.category,
#             identification_number=archive_product.identification_number,
#             unit_of_measurement=archive_product.unit_of_measurement,
#             quantity=archive_product.quantity,
#             price=archive_product.price,
#             status=archive_product.status
#         )
#         new_product.save()
#         archive_product.delete()
#
#         return Response(data=ProductSerializers(new_product).data, status=status.HTTP_201_CREATED)
