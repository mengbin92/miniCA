from django.urls import path

from .import views

app_name = 'CA'
urlpatterns = [
    path('',views.index,name='index'),
    path('csr',views.CSR,name='csr'),
]