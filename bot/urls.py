from django.urls import path, include
from bot import views

urlpatterns = [
    path('', views.ChatView.as_view()),
]
