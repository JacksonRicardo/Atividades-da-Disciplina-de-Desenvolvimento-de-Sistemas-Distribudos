from django.shortcuts import get_object_or_404, render
from rest_framework import serializers

from app.models import Todo
from app.serializers import TodoSerializer

from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer