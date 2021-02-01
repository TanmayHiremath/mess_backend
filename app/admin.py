from django.contrib import admin
from .models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):

    list_display = ('name', 'roll_number', 'status')

admin.site.register(User, UserAdmin)
