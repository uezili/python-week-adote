from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pests, name="listar_pets")
]
