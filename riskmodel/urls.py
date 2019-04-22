from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('risk_item/', views.risk_item, name='risk_item'),
    path('get_info/', views.start, name='start'),
]