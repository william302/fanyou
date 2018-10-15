from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('ajax/send_verify_code/', views.send_verify_code, name='send_verify_code'),
    path('signup_success/', views.signup_success, name='signup_success'),
    path('merchants/', views.merchants, name='merchants'),
    path('merchant_detail/<int:merchant_id>/', views.merchant_detail, name='merchant_detail')
]