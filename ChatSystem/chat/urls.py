# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('select/', views.group_selection, name = 'group_selection'),
    path('create/', views.create_group, name = 'create_group'),
    path('', views.index, name='index'),
    path('room/<str:room_name>/', views.room, name = 'room')
]
