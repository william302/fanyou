from django.urls import path
from . import views

urlpatterns = [
    path('', views.vote_index, name='vote_index'),
    path('ajax/vote/<int:candidate_id>/', views.vote, name='vote'),
    path('ajax/lazy_load_candidates/', views.lazy_load_candidates, name='lazy_load_candidates'),
    path('candidate_detail/<int:candidate_id>/', views.candidate_detail, name='candidate_detail'),
    path('vote_login/', views.vote_login, name='vote_login'),

]