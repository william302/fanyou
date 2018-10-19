from django.urls import path
from . import views

urlpatterns = [
    path('api/merchant/qrcodes', views.qrcode, name='qrcode'),

]