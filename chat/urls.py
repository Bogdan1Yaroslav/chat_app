from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('login/', views.LogInView.as_view(), name="login"),
    path("logout/", views.LogOutView.as_view(), name="logout"),
    path('select_chat/', views.select_chat, name='select_chat'),
    path('chat/<str:room_name>/', views.room, name='room'),


]
