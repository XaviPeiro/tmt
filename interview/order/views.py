from rest_framework import mixins

from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer

class OrderDeactivateView(GenericAPIView, mixins.UpdateModelMixin):
    # This is not following the apparent REST design, but the assignment sounds like we want an action in here.
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'


    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.is_active = False
        instance.save()
        serializer = self.get_serializer(instance)

        return Response(serializer.data, status=200)