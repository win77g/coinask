from django.shortcuts import render
import http.client
from rest_framework.views import APIView
from rest_framework import viewsets,permissions,status
from rest_framework.response import Response
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from GoogleNews import GoogleNews

class CoinDetail(APIView):
    permission_classes = [permissions.AllowAny, ]
      
    def get(self, request, format=None):
        coin = request.query_params['coin']  
        
        # url = 'https://api.coincap.io/v2/assets/{}/history?interval=d1'.format(coin)
        url = 'https://api.coingecko.com/api/v3/coins/{}/market_chart?vs_currency=usd&days=max'.format(coin)
        headers = {
                 'Accepts': 'application/json',
                 }
        session = Session()
        session.headers.update(headers)
        try: 
           response = session.get(url)
        #    data = json.loads(response.text)
           response.raise_for_status()  # raises exception when not a 2xx response
           if response.status_code != 204:
               data = response.json()
               data = data['prices']
               
        #    data = data['data']
        #    q=[]
        #    w=[] * 1
        #    e=[]
        #    for p in data:
        #        q.append([*p.values()]) #оставляем только значения
        #    for i in q:
        #        w.append(i)
        #    for r in w:
        #        del r[2]  #удаляем лишний элемент
        #        r[0],r[1] = r[1],r[0] #меняем местами
        #        e.append(r)
        #    q.clear()
        #    w.clear
           return Response(data, status=status.HTTP_200_OK) 
        except (ConnectionError, Timeout, TooManyRedirects) as z:
           print(z) 

# chart on 7 days
class CoinMiniChart(APIView):
    permission_classes = [permissions.AllowAny, ]
      
    def get(self, request, format=None):
        coin = request.query_params['coin']  
        
        url = 'https://api.coingecko.com/api/v3/coins/{}/market_chart?vs_currency=usd&days=0.05'.format(coin)
        headers = {
                 'Accepts': 'application/json',
                 }
        session = Session()
        session.headers.update(headers)
        try: 
           response = session.get(url)
        #    data = json.loads(response.text)
           response.raise_for_status()  # raises exception when not a 2xx response
           if response.status_code != 204:
               data = response.json()
               data = data['prices']
               
       
           return Response(data, status=status.HTTP_200_OK) 
        except (ConnectionError, Timeout, TooManyRedirects) as z:
           print(z) 


class CoinDetailAllMarket(APIView):
    permission_classes = [permissions.AllowAny, ]
      
    def get(self, request, format=None):
        coin = request.query_params['coin']  
       
        # url = 'https://api.coincap.io/v2/assets/{}/markets'.format(coin)
        url = 'https://api.coingecko.com/api/v3/coins/{}/tickers?page=1'.format(coin)
        headers = {
                 'Accepts': 'application/json',
                #  'User-agent': 'your bot 0.1'
                 }
        session = Session()
        session.headers.update(headers)
        try: 
           response = session.get(url)
        #    data = json.loads(response.text)
           response.raise_for_status()  # raises exception when not a 2xx response
           if response.status_code != 204:
               data = response.json()              
               data = data['tickers']
               data.sort(key=lambda x: (x['converted_volume']['usd']),reverse=True)
            #    print(data)
               return Response(data, status=status.HTTP_200_OK) 
        except (ConnectionError, Timeout, TooManyRedirects) as z:
           print(z)           
# Create your views here.
class CoinDetailInfo(APIView):
      permission_classes = [permissions.AllowAny, ]
      def get(self, request, format=None):
          coin = request.query_params['coin'] 
          
          url = 'https://api.coingecko.com/api/v3/coins/{}/'.format(coin)
         
          headers = {
                 'Accepts': 'application/json',
                 
                         }

          session = Session()
          session.headers.update(headers)
           
          try:
            
            response = session.get(url)
            data = json.loads(response.text)
            
            
            return Response(data, status=status.HTTP_200_OK) 
            # results = self.paginate_queryset(data, request, view=self)

           
          
          except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

class CryptoNews(APIView):
      permission_classes = [permissions.AllowAny, ]
      def get(self, request, format=None):
          coin = request.query_params['coin']
          try:
            googlenews = GoogleNews(lang='en', period='1d')
            # googlenews.search('machine learning')
            googlenews.get_news(coin)
            results = googlenews.results(sort=False)
            results.sort(key=lambda x: (x['date']),reverse=False)
            data = []
            for i in results:
               if coin in i['title']:
                  data.append(i)
            return Response(data, status=status.HTTP_200_OK) 
            # results = self.paginate_queryset(data, request, view=self)

           
          
          except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
          