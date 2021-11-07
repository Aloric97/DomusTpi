from django.urls import path
from .views import IniciarSesion

urlpatterns = [
    path("internauta/login", IniciarSesion, name="login"),
]
