from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from app import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

admin.site.site_header = 'Tinkerer\'s Lab Admin '

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    
#     path("autho/", views.posts),
#     path('requestss/', views.RequestSearch.as_view()),
#     path('requestsd/', views.RequestDate.as_view()),
#     path('itemss/', views.ItemSearch.as_view()),
#     path("sendmail/<str:roll_number>", views.sendMail.as_view()),
#     path("customer/<str:roll_number>",views.getCustomer.as_view()),
#     path("mail/<str:roll_number>",views.getMail.as_view()),
#     path("auth_technician/",views.authenticate_technician),
#     path("change_pwd/",views.change_pwd),
#     path('fblinkss/', views.FblinkSearch.as_view()),
#     path('machiness/', views.MachineSearch.as_view()),


]
# if settings.DEBUG == True: 
#         urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)