from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
# def main(request):
#     return HttpResponse("Hello")

class RoomView(generics.CreateAPIView):
    # here try to use generics.ListAPIView
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    