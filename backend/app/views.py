from app.serializers import MonthSerializer, UserSerializer
from django.shortcuts import render
from rest_framework import viewsets, generics, status
from django.http import JsonResponse
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
import urllib
import csv
from datetime import datetime
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def init_users(self, request, pk=None):
        url = request.data['url']
        print(url)
        print(":next")
        response = urllib.request.urlopen(url)
        reader = csv.DictReader(response.read().decode('utf-8').splitlines())
        header = ["name", "roll_number", "status", "card_no","image_url"]

        if request.data['mode'] == 'create':
            for each in reader:
                print(each)
                row = {}
                for field in header:
                    row[field] = each[field]
                serializer = UserSerializer(data=row)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.data['mode'] == 'update':
            for each in reader:
                print(each)
                row = {}
                user = User.objects.get(pk=each["roll_number"])
                for field in header:
                    row[field] = each[field]
                serializer = UserSerializer(user, data=row)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=None, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MonthViewSet(viewsets.ModelViewSet):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer

    @action(detail=False, methods=['post'])
    def allow_meal(self, request):
        print(request.data)
        user = User.objects.get(card_no=request.data['card_no'])
        current_month = datetime.now().strftime('%m')
        date = int(datetime.now().strftime('%d'))
        meal_no = int(request.data['meal_no'])
        month_data = Month.objects.get(
            roll_number=user.roll_number, month=current_month)
        print(month_data.data[date-1][meal_no])
        if(month_data.data[date-1][meal_no] == '9'):
            data = list(month_data.data[date-1])
            data[meal_no] = '2'
            month_data.data[date-1] = ''.join(data)
            month_data.save()
            return JsonResponse({"allow": "1","remark":"Give meal number {} to {}".format(meal_no,user.name)})
        elif(month_data.data[date-1][meal_no] == '2'):
            return JsonResponse({"allow": "0","remark":"Don't give meal. Already taken"})


def find_meal_no(request):
    def objectify(obj):
        return datetime.strptime(obj, '%I:%M%p').time()
    ###########################
    breakfast_start = '12:01AM'
    breakfast_end = '9:30AM'
    lunch_start = '12:30PM'
    lunch_end = '2:00PM'
    tiffin_start = '4:30PM'
    tiffin_end = '6:15PM'
    dinner_start = '7:30PM'
    dinner_end = '11:30PM'
    ##############################
    current_time = datetime.now().time()
    if (objectify(breakfast_start) <= current_time <= objectify(breakfast_end)):
        i = 1
    elif (objectify(lunch_start) <= current_time <= objectify(lunch_end)):
        i = 2
    elif (objectify(tiffin_start) <= current_time <= objectify(tiffin_end)):
        i = 3
    elif (objectify(dinner_start) <= current_time <= objectify(dinner_end)):
        i = 4
    else:
        i = 9
    return JsonResponse({'meal_no': i})
