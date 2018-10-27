from django.urls import path
from . import views

urlpatterns = [
    path('merchant/qrcodes', views.qrcode, name='qrcode'),
]
