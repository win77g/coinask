from django.shortcuts import render
from .models import *
from rest_framework import viewsets,permissions
from .serializers import *

class StakingCoinViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = StakingCoin.objects.all()
    serializer_class = StakingCoinSerializer
