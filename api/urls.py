from django.urls import path
from .import views

urlpatterns = [
    path('key', views.KeyList.as_view()),
    path('key/<int:pk>', views.KeyDetial.as_view()),
]
