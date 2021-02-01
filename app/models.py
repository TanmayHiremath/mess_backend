from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    roll_number = models.CharField(max_length=12,primary_key=True)
    status = models.CharField(max_length=15)
    card_no = models.CharField(max_length=50)
