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
