from rest_framework import serializers
from .models import KeyModel, CRLModel, CertificateModel, CSRModel


class KeyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = KeyModel
        fields = ('id', 'asymmetric_alg', 'bits', 'key_pass')


class KeyDetialSerializer(serializers.ModelSerializer):

    class Meta:
        model = KeyModel
        fields = ('id', 'asymmetric_alg', 'bits',
                  'key_pass', 'key_private', 'key_public', 'used')


class CSRListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSRModel
        fields = ('id', 'common', 'country', 'province',
                  'locality', 'organization', 'organizationunit', 'email', 'days', 'role')


class CSRDetialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSRModel
        fields = ('id', 'common', 'country', 'province',
                  'locality', 'organization', 'organizationunit', 'email', 'days', 'role', 'content', 'created')


class CertListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateModel
        fields = ('id', 'serial', 'valid')


class CertDetialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateModel
        fields = ('id', 'serial', 'content', 'created', 'valid')
