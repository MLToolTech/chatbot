from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from .models import ChatTransactionModel
from .serializers import ChatTransactionSerializer


class ChatView(generics.CreateAPIView):
    queryset = ChatTransactionModel.objects.all()
    serializer_class = ChatTransactionSerializer
