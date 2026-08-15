from django.urls import path
from .views import receber_arquivo

urlpatterns= [
    path('', receber_arquivo, name='receber_arquivo'),
]