from app.serializers import UserSerializer
from django.shortcuts import render
from rest_framework import viewsets, generics,status
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import action
import urllib
import csv
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False,methods=['post'])
    def init_users(self, request, pk=None):
      url=request.data['url']
      print(url)
      print(":next")
      response = urllib.request.urlopen(url)
      reader = csv.DictReader( response.read().decode('utf-8').splitlines() )
      header= [ "name","roll_number","status","card_no"]
   
      
      if request.data['mode']=='create':
            for each in reader:
                  print(each)
                  row={}
                  for field in header:
                        row[field]=each[field]
                  serializer = UserSerializer(data=row)
                  if serializer.is_valid():
                        serializer.save()
                  else:
                              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      elif request.data['mode']=='update':
            for each in reader:
                  print(each)
                  row={}
                  user = User.objects.get(pk=each["roll_number"])
                  for field in header:
                        row[field]=each[field]
                  serializer = UserSerializer(user,data=row)
                  if serializer.is_valid():
                        serializer.save()
                  else:
                              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                       

      return Response(data=None, status=status.HTTP_201_CREATED)
      # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    