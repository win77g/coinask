from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets,permissions,status
from rest_framework.response import Response
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .pagination import PostPageNumberPagination
import json
from django.core.paginator import Paginator
import os.path
# Create your views here.


class MarketCapList(APIView,PostPageNumberPagination):
      permission_classes = [permissions.AllowAny, ]
      def get(self, request, format=None):
          url = 'https://api.coingecko.com/api/v3/coins/'
   
          headers = {
                 'Accepts': 'application/json',
               #   'X-CMC_PRO_API_KEY': 'ef37df52-70bb-448c-b058-a985c7f337ae',
                         }

          session = Session()
          session.headers.update(headers)
           
          try:
            
            response = session.get(url)
            data = json.loads(response.text)
            print(data)
            data = data['data']
            print(type(request.query_params['sort']))
            results = self.paginate_queryset(data, request, view=self)

             
            if(request.query_params['sort']=='up'):
               results.sort(key=lambda x: (x['quote']['USD']['percent_change_1h']),reverse=True)
               return Response(results, status=status.HTTP_200_OK)
            if(request.query_params['sort']=='down'):
               results.sort(key=lambda x: (x['quote']['USD']['percent_change_1h']),reverse=False)
               return Response(results, status=status.HTTP_200_OK)   
            if(request.query_params['sort'] , None):
               return Response(results, status=status.HTTP_200_OK)  
          
          except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

class CoinGechkoCoinList(APIView,PostPageNumberPagination):
    permission_classes = [permissions.AllowAny, ]
      
    def get(self, request, format=None):
        page = request.query_params['page']
        url = 'https://api.coingecko.com/api/v3/coins/?page={}'.format(page)
      
        headers = {
                 'Accepts': 'application/json',
                 }
        session = Session()
        session.headers.update(headers)
        try: 
           response = session.get(url)
           data = json.loads(response.text)
         
           return Response(data, status=status.HTTP_200_OK) 
     
        except (ConnectionError, Timeout, TooManyRedirects) as z:
           print(z)           
# Create your views here.            

class SearchCoin(APIView):
      permission_classes = [permissions.AllowAny, ]
      def get(self, request, format=None):
          coin = request.query_params['coin']
         #  coin = coin.title()
          print(coin)
          #f = open("coinsSymbol.json",'r')
#f.write(str(to_json))
          with open('coinsSymbol.json', 'r') as f:
                  m = json.load(f)
  
          m = m['coins']

          qw = list(filter(lambda person: person['name'] == coin, m))
          print(len(qw))
          if len(qw) == 1:
             coinId = qw[0]['id']
             url = 'https://api.coingecko.com/api/v3/coins/{}/'.format(coinId)
             headers = {'Accepts': 'application/json',}
             session = Session()
             session.headers.update(headers)
             try:
               response = session.get(url)
               data = json.loads(response.text)
               return Response(data, status=status.HTTP_200_OK) 
             except (ConnectionError, Timeout, TooManyRedirects) as e:
               print(e)
          if len(qw) == 0:
             qw = list(filter(lambda person: person['symbol'] == coin, m))
             print(qw)
             coinId = qw[0]['id']
             url = 'https://api.coingecko.com/api/v3/coins/{}/'.format(coinId)
             headers = {'Accepts': 'application/json',}
             session = Session()
             session.headers.update(headers)
             try:
               response = session.get(url)
               data = json.loads(response.text)
               return Response(data, status=status.HTTP_200_OK) 
             except (ConnectionError, Timeout, TooManyRedirects) as e:
               print(e)