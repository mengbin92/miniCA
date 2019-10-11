from rest_framework import serializers
from .models import KeyModel, CRLModel, CertificateModel, CSRModel
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class UserDetialSerializer(serializers.ModelSerializer):

    #owner = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')


class KeyListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = KeyModel
        fields = ('id', 'asymmetric', 'bits', 'key_pass')


class KeyDetialSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = KeyModel
        fields = ('id', 'asymmetric', 'bits',
                  'key_pass', 'key_private', 'key_public', 'used')


class CSRListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CSRModel
        fields = ('id', 'common', 'country', 'province',
                  'locality', 'organization', 'organizationunit', 'email', 'days', 'role')


class CSRDetialSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CSRModel
        fields = ('id', 'common', 'country', 'province',
                  'locality', 'organization', 'organizationunit', 'email', 'days', 'role', 'content', 'created')


class CertListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CertificateModel
        fields = ('id', 'serial', 'valid')


class CertDetialSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CertificateModel
        fields = ('id', 'serial', 'content', 'created', 'valid')
