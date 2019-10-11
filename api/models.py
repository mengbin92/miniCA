from django.db import models

# Create your models here.


class KeyModel(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='Key', on_delete=models.CASCADE)
    asymmetric = models.CharField(default='RSA', max_length=32)
    bits = models.IntegerField(default=2048)
    key_type = models.CharField(default='PEM', max_length=3)
    key_private = models.TextField()
    key_pass = models.CharField(max_length=256)
    key_public = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)


class CSRModel(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='CSR', on_delete=models.CASCADE)
    key = models.ForeignKey(KeyModel, on_delete=models.CASCADE)
    common = models.CharField(max_length=20, default='common')
    country = models.CharField(max_length=2, default='CN')
    province = models.CharField(max_length=20, default='shanxi')
    locality = models.CharField(max_length=20, default='yuncheng')
    organization = models.CharField(max_length=20, default='organization')
    organizationunit = models.CharField(
        max_length=20, default='organizationunit')
    email = models.EmailField(default='test@gmail.com')
    content_type = models.CharField(default='PEM', max_length=3)
    content = models.TextField()
    days = models.IntegerField(default=730)
    role = models.CharField(max_length=10, default='user')
    created = models.DateTimeField(auto_now_add=True)
    signed = models.BooleanField(default=False)


class CertificateModel(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='Certificate', on_delete=models.CASCADE)
    key = models.ForeignKey(KeyModel, on_delete=models.CASCADE)
    csr = models.ForeignKey(CSRModel, on_delete=models.CASCADE)
    serial = models.CharField(max_length=64)
    content_type = models.CharField(default='PEM', max_length=3)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    valid = models.BooleanField(default=True)


class CRLModel(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='CRL', on_delete=models.CASCADE)
    serial = models.CharField(max_length=64)
    reason = models.CharField(max_length=256)
    signed = models.BooleanField(default=False)
