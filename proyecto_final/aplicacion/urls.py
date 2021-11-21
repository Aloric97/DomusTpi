from django.urls import path
from .views import IniciarSesion, ProgramarCita, TurnosDados, CancelarCita

urlpatterns = [
    path("internauta/login", IniciarSesion, name="login"),
    path("Secretaria/programar_cita", ProgramarCita, name="programar_cita"),
    path("Secretaria/turnos_dados", TurnosDados, name="turnos_dados"),
    path("turnos_dados/<int:cita>", CancelarCita, name="cancelar_cita"),
]
