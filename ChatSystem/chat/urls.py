# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('select/', views.group_selection, name = 'group_selection'),
    path('create/', views.create_group, name = 'create_group'),
    path('', views.index, name='index'),
    path('room/<str:room_id>/', views.room, name = 'room'),
    path('ajax/check', views.in_group, name = 'check_in_group')
]
