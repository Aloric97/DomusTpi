from django.urls import path
from .views import IniciarSesion, ProgramarCita, TurnosDados, CancelarCita, EditarCita, Secretaria_Agenda

urlpatterns = [
    path("internauta/login", IniciarSesion, name="login"),
    path("programar_cita/<int:cliente_id>", ProgramarCita, name="programar_cita"),
    path("turnos_dados", TurnosDados, name="turnos_dados"),
    path("cancelar_cita/<int:cita>", CancelarCita, name="cancelar_cita"),
    path("editar_cita/<int:cita>", EditarCita, name="editar_cita"),
    path('agenda', Secretaria_Agenda, name='secretaria_agenda'),
]
