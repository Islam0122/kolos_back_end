from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse as json_resp
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from transaction.models import Order
from .serializers import OrderSerializer

# import seeder_beer as sd
#
#
# def seeder_start(request):
#     sd.seed()
#     return json_resp({'status': 'success'})


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'


# class ArchivedOrderView(ModelViewSet):
#     queryset = Order.objects.filter(is_archived=True)
#     serializer_class = OrderSerializer
#     lookup_field = 'pk'

