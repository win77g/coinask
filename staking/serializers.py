from .models import *
from rest_framework import serializers


class StakingCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = StakingCoin
        fields = ('name','logo','dayplan','procent','mindeposit','maxdeposit','is_active','updated')