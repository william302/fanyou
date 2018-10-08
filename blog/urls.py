from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    # path('test/', views.send_message, name='send_message'),
    path('ajax/send_verify_code/', views.send_verify_code, name='send_verify_code')
]