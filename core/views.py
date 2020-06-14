from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomerSerializer, ProfessionSerializer, DataSheetSerializer, DocumentSerializer

from .models import Customer, Profession, DataSheet, Document


# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    # Custom queryset method - get_queryset
    def get_queryset(self):
        # break point for debugging
        # import pdb
        # pdb.set_trace()

        # objects.filter(active=True) - only active customers, using filter method
        active_customers = Customer.objects.filter(active=True)
        return active_customers


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class DataSheetViewSet(viewsets.ModelViewSet):
    queryset = DataSheet.objects.all()
    serializer_class = DataSheetSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
