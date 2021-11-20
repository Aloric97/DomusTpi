from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import datetime

class User(AbstractUser):
      class Tipos(models.TextChoices):
          ADMINISTRADOR = "ADMINISTRADOR", "Administrador"
          CLIENTE = "CLIENTE", 'Cliente'
          SECRETARIA = "SECRETARIA", 'Secretaria'
          CAJERA = "CAJERA", 'Cajera'
          EMP_MARKETING = "EMP_MARKETING", 'Empleado Marketing'
          JE_COMER = "JE_COMER", 'Jefe Comercialización'
          JE_ADM = "JE_ADM", 'Jefe Administración'
          GERENTE = "GERENTE", 'Gerente'
          AGENTE_INMOBILIARIO = "AGENTE_INMOBILIARIO", 'Agente Inmobiliario'

      tipo = models.CharField(_("Tipo"), max_length=50, choices=Tipos.choices, default=Tipos.CLIENTE)

      def get_absolute_url(self):
          return reverse("users:detail", kwargs={"username": self.username})

      def __str__(self):
          return f"usuario: {self.username}, rol: {self.tipo}, pk: {self.pk}"

#clases necesarias para que un usuario no sea de todos los tipos.
class AdministradorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(tipo=User.Tipos.ADMINISTRADOR)

class ClienteManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(tipo=User.Tipos.CLIENTE)

class SecretariaManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(tipo=User.Tipos.SECRETARIA)

class CajeraManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(tipo=User.Tipos.CAJERA)

class EmpMarketingManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(tipo=User.Tipos.EMP_MARKETING)

class JeComerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(tipo=User.Tipos.JE_COMER)

class JeAdmManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(tipo=User.Tipos.JE_ADM)

class GerenteManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(tipo=User.Tipos.GERENTE)

class AgenteManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(tipo=User.Tipos.AGENTE_INMOBILIARIO)


#si la fila no existe (pk) en la bd, se guarda el usuario con el tipo correspondiente


class Administrador(User):
    objects = AdministradorManager()
    class Meta:
        proxy = True # los proxy models no crean nuevas tablas, toman los datos desde User

    def save(self, *args, **kwargs):
        if not self.pk:
            self.tipo = User.Tipos.ADMINISTRADOR
        return super().save(*args, **kwargs)


class Cliente(User):
    objects = ClienteManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.tipo = User.Tipos.CLIENTE
        return super().save(*args, **kwargs)


class Secretaria(User):
    objects = SecretariaManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.tipo = User.Tipos.SECRETARIA
        return super().save(*args, **kwargs)


class Cajera(User):
    objects = CajeraManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.tipo = User.Tipos.CAJERA
        return super().save(*args, **kwargs)

class EmpMarketing(User):
    objects = EmpMarketingManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.tipo = User.Tipos.EMP_MARKETING
        return super().save(*args, **kwargs)


class JeComercializacion(User):
    objects = JeComerManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.tipo = User.Tipos.JE_COMER
        return super().save(*args, **kwargs)


class JeAdministracion(User):
    objects = JeAdmManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.tipo = User.Tipos.JE_ADM
        return super().save(*args, **kwargs)


class Gerente(User):
    objects = GerenteManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.tipo = User.Tipos.GERENTE
        return super().save(*args, **kwargs)

class Agente(User):
    objects = AgenteManager()

    class Meta:
        proxy = True
    def __str__(self):
        return f"{self.first_name} {self.last_name} - ID: {self.pk}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.tipo = User.Tipos.AGENTE_INMOBILIARIO
        return super().save(*args, **kwargs)

class Turno(models.Model):
    TURNOS_HORARIOS = (
        ("8:00", "8:00"),
        ("8:30", "8:30"),
        ("9:00", "9:00"),
        ("9:30", "9:30"),
        ("10:00", "10:00"),
        ("10:30", "10:30"),
        ("11:00", "11:00"),
        ("11:30", "11:30"),
    )

    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, related_name="agente_turno")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="cliente_turno")
    dia = models.CharField(max_length=255)
    hora = models.CharField(max_length=20, choices=TURNOS_HORARIOS)


    def getTurnosDados(fecha=None):
        turnos_ordenados = Turno.objects.order_by('dia', 'hora')
        turnos_dados = []
        if fecha != " 5" and fecha != "":
            for turno in turnos_ordenados:
                if turno.dia.replace("/", "") == str(fecha).replace("-", ""):
                    turnos_dados.append(turno)
            return turnos_dados

        for turno in turnos_ordenados:
            turnos_dados.append(turno)
        return turnos_dados

    def getAgentesDisponibles(fecha, hora):
        agentes_ocupados = []
        agentes_disponibles = []
        for turno in Turno.objects.all():
            if turno.dia.replace("/", "") == fecha and turno.hora == hora:
                agentes_ocupados.append(turno.agente)
        for agente in Agente.objects.all():
            if agente not in agentes_ocupados:
                agentes_disponibles.append(agente)
        return agentes_disponibles

    def getHorariosDisponibles(fecha):
        horarios_disponibles = {}
        for horario in Turno.TURNOS_HORARIOS:
            horarios_disponibles.setdefault(horario[0], Turno.getAgentesDisponibles(fecha, horario[0]))
        return horarios_disponibles

    def getProximosTurnos(cantidad):
        proximos_turnos = {}
        for i in range(cantidad):
            fecha = str(datetime.date.today()+ datetime.timedelta(days=i))
            fecha = fecha.replace("-", "")
            proximos_turnos.setdefault(fecha, Turno.getHorariosDisponibles(fecha))
        return proximos_turnos

    def estaDisponible(fecha, hora, agente):
        for turno in Turno.objects.all():
            if turno.dia == fecha and turno.hora == hora and int(agente) == turno.agente.id:
                return False
        return True

    def __str__(self):
        return f"Agente: {self.agente.username}, Cliente: {self.cliente.username} - Fecha: {self.dia} {self.hora}"
