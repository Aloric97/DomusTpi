from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

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
          return f"usuario: {self.username}, rol: {self.tipo}, pk: {self.pk} "

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
