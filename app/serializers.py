from django.db.models import fields
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
      class Meta:
            model= User
            fields='__all__'
class MonthSerializer(serializers.ModelSerializer):
      class Meta:
            model= Month
            fields='__all__'