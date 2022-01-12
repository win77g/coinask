from django.shortcuts import render
import http.client
from rest_framework.views import APIView
from rest_framework import viewsets,permissions,status
from rest_framework.response import Response
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class ExchangeDetail(APIView):
    permission_classes = [permissions.AllowAny, ]
      
    def get(self, request, format=None):
        ex = request.query_params['exchange']  
        url = 'https://api.coingecko.com/api/v3/exchanges/{}'.format(ex)
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
            #    data = data['prices']
    
           return Response(data, status=status.HTTP_200_OK) 
        except (ConnectionError, Timeout, TooManyRedirects) as z:
           print(z) 

class ExchangeValume(APIView):
    permission_classes = [permissions.AllowAny, ]
      
    def get(self, request, format=None):
        ex = request.query_params['exchange']  
        url = 'https://api.coingecko.com/api/v3/exchanges/{}/volume_chart?days=360'.format(ex)
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
           return Response(data, status=status.HTTP_200_OK) 
        except (ConnectionError, Timeout, TooManyRedirects) as z:
           print(z) 