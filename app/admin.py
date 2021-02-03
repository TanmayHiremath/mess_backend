from django.contrib import admin
from .models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):

    list_display = ('name', 'roll_number', 'status','image_file','image_tag')
class MonthAdmin(admin.ModelAdmin):

    list_display = ('month', 'roll_number', 'data')
admin.site.register(User, UserAdmin)
admin.site.register(Month,MonthAdmin)
