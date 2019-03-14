from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .serializers import KeyListSerializer, KeyDetialSerializer
from .models import KeyModel, CertificateModel, CRLModel, CSRModel
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics


class KeyList(generics.ListCreateAPIView):
    queryset = KeyModel.objects.all()
    serializer_class = KeyListSerializer


class KeyDetial(generics.RetrieveAPIView):
    queryset = KeyModel.objects.all()
    serializer_class = KeyDetialSerializer
