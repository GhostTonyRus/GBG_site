from django.shortcuts import render
from rest_framework import generics
from .models import Application
from .serializer import ApplicationSerializer
# Create your views here.

class ApplicationApiView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()


