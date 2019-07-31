from rest_framework import serializers
from .models import Bankprod

class BankprodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bankprod
        fields = '__all__'