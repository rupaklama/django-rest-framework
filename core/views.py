from django.shortcuts import render

from rest_framework import viewsets, filters
from rest_framework.response import Response

from .serializers import CustomerSerializer, ProfessionSerializer, DataSheetSerializer, DocumentSerializer
from rest_framework.decorators import action

from .models import Customer, Profession, DataSheet, Document


# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    # using DjangoFilterBackend - search filters
    filter_backends = [filters.SearchFilter]
    search_fields = ('name', 'address')

    # http://localhost:8000/api/customers/?ordering=id
    ordering_fields = ('name', )  # ordering by id
    ordering = ('id', )  # default ordering

    # hiding pk-id in detail view
    # lookup_field = 'email'  # unique field like id

    # Custom queryset method - get_queryset
    def get_queryset(self):
        # break point for debugging
        # import pdb
        # pdb.set_trace()

        # objects.filter(active=True) - only active customers, using filter method
        active_customers = Customer.objects.filter(active=True)
        return active_customers

    # custom method using action to deactivate customer
    @action(detail=True)  # decorator, detail=True means method will execute in detail view
    def deactivate(self, request, **kwargs):
        customer = self.get_object()
        customer.active = False
        customer.save()

        # serialize customer
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class DataSheetViewSet(viewsets.ModelViewSet):
    queryset = DataSheet.objects.all()
    serializer_class = DataSheetSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
