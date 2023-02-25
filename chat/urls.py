from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.LogInView.as_view(), name="login"),
    path('select_chat/', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),


]
