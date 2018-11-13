from django.urls import path
from . import views

app_name = 'wechat'
urlpatterns = [
    path('', views.index, name='index'),
]