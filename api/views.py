from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from .serializers import KeyListSerializer, KeyDetialSerializer, CertDetialSerializer, CertListSerializer, CSRDetialSerializer, CSRListSerializer, UserSerializer, UserDetialSerializer
from .models import KeyModel, CertificateModel, CRLModel, CSRModel
from .permissions import IsOwnerOrReadOnly
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework import generics

from cert.certopt import generatekey

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = UserDetialSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(
                username=serializer['username'].value,
                password=serializer['password'].value,
                email=serializer['email'].value
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetial(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetialSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class KeyList(generics.ListCreateAPIView):
    queryset = KeyModel.objects.all()
    serializer_class = KeyListSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def post(self, request, format=None):
        serializer = KeyListSerializer(data=request.data)
        try:
            user = User.objects.get(username=request.user)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if serializer.is_valid():
            asy = serializer['asymmetric'].value
            bits = int(serializer['bits'].value)
            key_pass = serializer['key_pass'].value

            key = generatekey(asy,bits)

            db_key = KeyModel()
            db_key.owner = user
            db_key.asymmetric = asy
            db_key.bits = bits
            db_key.key_pass = key_pass
            


class KeyDetial(generics.RetrieveAPIView):
    queryset = KeyModel.objects.all()
    serializer_class = KeyDetialSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class CSRList(generics.ListCreateAPIView):
    queryset = CSRModel.objects.all()
    serializer_class = CSRListSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class CSRDetial(generics.RetrieveAPIView):
    queryset = CSRModel.objects.all()
    serializer_class = CSRDetialSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class CertList(generics.ListCreateAPIView):
    queryset = CertificateModel.objects.all()
    serializer_class = CertListSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class CertDetial(generics.RetrieveAPIView):
    queryset = CertificateModel.objects.all()
    serializer_class = CertDetialSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
