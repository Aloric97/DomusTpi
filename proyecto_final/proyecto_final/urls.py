"""proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from aplicacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Principal, name='Principal'),
    path('logout/', views.logoutUser, name='logout'),
    path("", include("aplicacion.urls"), name="perfiles"),


    path('AdministradorWeb/AddUser',views.AdministradorWeb_AddUser, name='AdministradorWeb_agregar_usuario'),
    path('AdministradorWeb/DatosPropiedad',views.AdministradorWeb_DatosPropiedad, name='AdministradorWeb_DatosPropiedad'),
    path('AdministradorWeb/EliminarUsuario',views.AdministradorWeb_EliminarUsuario, name='AdministradorWeb_EliminarUsuario'),
    path('AdministradorWeb/Inmuebles',views.AdministradorWeb_Inmuebles, name='AdministradorWeb_Inmuebles'),
    path('AdministradorWeb/Principal',views.AdministradorWeb_Principal, name='AdministradorWeb_Principal'),


    path('agenteInmobiliario/Agenda',views.agenteInmobiliario_Agenda, name='agenteInmobiliario_Agenda'),
    path('agenteInmobiliario/carga',views.agenteInmobiliario_carga, name='agenteInmobiliario_carga'),
    path('agenteInmobiliario/cargaJekyll',views.agenteInmobiliario_cargaJekyll, name='agenteInmobiliario_cargaJekyll'),
    path('agenteInmobiliario/DatosPropiedad',views.agenteInmobiliario_DatosPropiedad, name='agenteInmobiliario_DatosPropiedad'),
    path('agenteInmobiliario/Inmuebles',views.agenteInmobiliario_Inmuebles, name='agenteInmobiliario_Inmuebles'),
    path('agenteInmobiliario/Principal',views.agenteInmobiliario_Principal, name='agenteInmobiliario_Principal'),


    path('Cajera/Alquileres',views.Cajera_Alquileres, name='Cajera_Alquileres'),
    path('Cajera/Cierre',views.Cajera_Cierre, name='Cajera_Cierre'),
    path('Cajera/DatosPropiedad',views.Cajera_DatosPropiedad, name='Cajera_DatosPropiedad'),
    path('Cajera/Inmuebles',views.Cajera_Inmuebles, name='Cajera_Inmuebles'),
    path('Cajera/Principal',views.Cajera_Principal, name='Cajera_Principal'),
    path('Cajera/Transacciones',views.Cajera_Transacciones, name='Cajera_Transacciones'),
    path('Cajera/Ventas',views.Cajera_Ventas, name='Cajera_Ventas'),


    path('ClienteRegistrado/DatosPropiedad',views.ClienteRegistrado_DatosPropiedad, name='ClienteRegistrado_DatosPropiedad'),
    path('ClienteRegistrado/Inmuebles',views.ClienteRegistrado_Inmuebles, name='ClienteRegistrado_Inmuebles'),
    path('ClienteRegistrado/Principal',views.ClienteRegistrado_Principal, name='ClienteRegistrado_Principal'),
    path('ClienteRegistrado/SolicitarCita',views.ClienteRegistrado_SolicitarCita, name='ClienteRegistrado_SolicitarCita'),


    path('EmpleadoMarketing/DatosPropiedad',views.EmpleadoMarketing_DatosPropiedad, name='EmpleadoMarketing_DatosPropiedad'),
    path('EmpleadoMarketing/Inmuebles',views.EmpleadoMarketing_Inmuebles, name='EmpleadoMarketing_Inmuebles'),
    path('EmpleadoMarketing/Principal',views.EmpleadoMarketing_Principal, name='EmpleadoMarketing_Principal'),


    path('GerenteGeneral/DatosPropiedad',views.GerenteGeneral_DatosPropiedad, name='GerenteGeneral_DatosPropiedad'),
    path('GerenteGeneral/Inmuebles',views.GerenteGeneral_Inmuebles, name='GerenteGeneral_Inmuebles'),
    path('GerenteGeneral/Principal',views.GerenteGeneral_Principal, name='GerenteGeneral_Principal'),
    path('GerenteGeneral/Reportes',views.GerenteGeneral_Reportes, name='GerenteGeneral_Reportes'),


    path('internauta/DatosPropiedad',views.internauta_DatosPropiedad, name='internauta_DatosPropiedad'),
    path('internauta/Inmuebles',views.internauta_Inmuebles, name='internauta_Inmuebles'),
    path('Principal', views.Principal, name='Principal'),
    path('internauta/register',views.internauta_register, name='internauta_register'),


    path('JefaAdministracion/DatosPropiedad',views.JefaAdministracion_DatosPropiedad, name='JefaAdministracion_DatosPropiedad'),
    path('JefaAdministracion/Inmuebles',views.JefaAdministracion_Inmuebles, name='JefaAdministracion_Inmuebles'),
    path('JefaAdministracion/Principal',views.JefaAdministracion_Principal, name='JefaAdministracion_Principal'),
    path('JefaAdministracion/Clientes',views.JefaAdministracion_Clientes, name='JefaAdministracion_Clientes'),
    path('JefaAdministracion/Reportes',views.JefaAdministracion_Reportes, name='JefaAdministracion_Reportes'),
    path('JefaAdministracion/Transacciones',views.JefaAdministracion_Transacciones, name='JefaAdministracion_Transacciones'),


    path('JefaComercializacion/DatosPropiedad',views.JefaComercializacion_DatosPropiedad, name='JefaComercializacion_DatosPropiedad'),
    path('JefaComercializacion/Inmuebles',views.JefaComercializacion_Inmuebles, name='JefaComercializacion_Inmuebles'),
    path('JefaComercializacion/Principal',views.JefaComercializacion_Principal, name='JefaComercializacion_Principal'),
    path('JefaComercializacion/Clientes',views.JefaComercializacion_Clientes, name='JefaComercializacion_Clientes'),
    path('JefaComercializacion/Reportes',views.JefaComercializacion_Reportes, name='JefaComercializacion_Reportes'),
    path('JefaComercializacion/Propiedades',views.JefaComercializacion_Propiedades, name='JefaComercializacion_Propiedades'),
    path('JefaComercializacion/Actuales',views.JefaComercializacion_Actuales, name='JefaComercializacion_Actuales'),
    path('JefaComercializacion/Agenda',views.JefaComercializacion_Agenda, name='JefaComercializacion_Agenda'),
    path('JefaComercializacion/Antiguos',views.JefaComercializacion_Antiguos, name='JefaComercializacion_Antiguos'),
    path('JefaComercializacion/ClientesHistorico',views.JefaComercializacion_ClientesHistorico, name='JefaComercializacion_ClientesHistorico'),
    path('JefaComercializacion/Historico',views.JefaComercializacion_Historico, name='JefaComercializacion_Historico'),
    path('JefaComercializacion/Vendidas',views.JefaComercializacion_Vendidas, name='JefaComercializacion_Vendidas'),



    path('Secretaria/AceptarSolicitud',views.Secretaria_AceptarSolicitud, name='Secretaria_AceptarSolicitud'),
    path('Secretaria/Agenda',views.Secretaria_Agenda, name='Secretaria_Agenda'),
    path('Secretaria/CancelarCita',views.Secretaria_CancelarCita, name='Secretaria_CancelarCita'),
    path('Secretaria/Clientes',views.Secretaria_Clientes, name='Secretaria_Clientes'),
    path('Secretaria/DatosPropiedad',views.Secretaria_DatosPropiedad, name='Secretaria_DatosPropiedad'),
    path('Secretaria/Editar',views.Secretaria_Editar, name='Secretaria_Editar'),
    path('Secretaria/EditarCita',views.Secretaria_EditarCita, name='Secretaria_EditarCita'),
    path('Secretaria/Inmuebles',views.Secretaria_Inmuebles, name='Secretaria_Inmuebles'),
    path('Secretaria/Principal',views.Secretaria_Principal, name='Secretaria_Principal'),
    path('Secretaria/Solicitudes',views.Secretaria_Solicitudes, name='Secretaria_Solicitudes'),

]
