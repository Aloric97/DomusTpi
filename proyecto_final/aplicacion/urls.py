from django.urls import path
from .views import IniciarSesion, ProgramarCita, AgendarCita, TurnosDados

urlpatterns = [
    path("internauta/login", IniciarSesion, name="login"),
    path("Secretaria/programar_cita", ProgramarCita, name="programar_cita"),
    path("Secretaria/agendar_cita", AgendarCita, name="agendar_cita"),
    path("Secretaria/turnos_dados", TurnosDados, name="turnos_dados")
]
