from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .serializers import KeyListSerializer, KeyDetialSerializer, CertDetialSerializer, CertListSerializer, CSRDetialSerializer, CSRListSerializer
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


class CSRList(generics.ListCreateAPIView):
    queryset = CSRModel.objects.all()
    serializer_class = CSRListSerializer


class CSRDetial(generics.RetrieveAPIView):
    queryset = CSRModel.objects.all()
    serializer_class = CSRDetialSerializer


class CertList(generics.ListCreateAPIView):
    queryset = CertificateModel.objects.all()
    serializer_class = CertListSerializer


class CertDetial(generics.RetrieveAPIView):
    queryset = CertificateModel.objects.all()
    serializer_class = CertDetialSerializer
