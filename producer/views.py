from django.shortcuts import render
from rest_framework import viewsets
from producer.serializers import Bankprod,BankprodSerializer


class BankprodViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Bankprod.objects.all()
    serializer_class = BankprodSerializer

