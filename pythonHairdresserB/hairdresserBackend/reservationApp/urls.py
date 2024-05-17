from django.urls import path
from .views import testJson,lista_napisow

urlpatterns = [
    path('test/', testJson),
    path('napisy/', lista_napisow),
]
