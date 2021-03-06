# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets          # add this
from .serializers import TodoSerializer      # add this
from .models import todo                     # add this

class TodoView(viewsets.ModelViewSet):       # add this
  serializer_class = TodoSerializer          # add this
  queryset = todo.objects.all()              # add this
