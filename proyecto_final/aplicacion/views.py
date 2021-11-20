from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import Group

from .forms import LoginForm, CreateUserForm, ProgramarCitaForm
from .models import Turno, Cliente, Agente
from datetime import datetime

def IniciarSesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        usuario = request.POST['username']
        contraseña = request.POST['password']
        usuario = authenticate(username=usuario, password=contraseña)

        if usuario is not None:
            if usuario.is_active:
                login(request, usuario)
                return redirect("Principal")

        else:
            messages.error(request,'Usuario o contraseña incorrectos.')
            return redirect('login')

        if request.user.groups.filter(name='administradorWeb').exists():
            def homeDoctor(request):
                return redirect("AdministradorWeb_Principal")

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def index(request):
    context = {}
    return render(request, 'index.html',context)


def logoutUser(request):
    logout(request)
    return redirect('Principal')



def AdministradorWeb_AddUser(request):
    context = {}
    return render(request, 'AdministradorWeb/AddUser.html',context)

def AdministradorWeb_DatosPropiedad(request):
    context = {}
    return render(request, 'AdministradorWeb/DatosPropiedad.html',context)

def AdministradorWeb_EliminarUsuario(request):
    context = {}
    return render(request, 'AdministradorWeb/EliminarUsuario.html',context)

def AdministradorWeb_Inmuebles(request):
    context = {}
    return render(request, 'AdministradorWeb/Inmuebles.html',context)

def AdministradorWeb_Principal(request):
    context = {}
    return render(request, 'AdministradorWeb/Principal.html',context)





def agenteInmobiliario_Agenda(request):
    context = {}
    return render(request, 'agenteInmobiliario/Agenda.html',context)

def agenteInmobiliario_carga(request):
    context = {}
    return render(request, 'agenteInmobiliario/carga.html',context)

def agenteInmobiliario_cargaJekyll(request):
    context = {}
    return render(request, 'agenteInmobiliario/cargaJekyll.html',context)

def agenteInmobiliario_DatosPropiedad(request):
    context = {}
    return render(request, 'agenteInmobiliario/DatosPropiedad.html',context)

def agenteInmobiliario_Inmuebles(request):
    context = {}
    return render(request, 'agenteInmobiliario/Inmuebles.html',context)

def agenteInmobiliario_Principal(request):
    context = {}
    return render(request, 'agenteInmobiliario/Principal.html',context)








def Cajera_Alquileres(request):
    context = {}
    return render(request, 'Cajera/Alquileres.html',context)

def Cajera_Cierre(request):
    context = {}
    return render(request, 'Cajera/Cierre.html',context)

def Cajera_DatosPropiedad(request):
    context = {}
    return render(request, 'Cajera/DatosPropiedad.html',context)

def Cajera_Inmuebles(request):
    context = {}
    return render(request, 'Cajera/Inmuebles.html',context)

def Cajera_Principal(request):
    context = {}
    return render(request, 'Cajera/Principal.html',context)

def Cajera_Transacciones(request):
    context = {}
    return render(request, 'Cajera/Transacciones.html',context)

def Cajera_Ventas(request):
    context = {}
    return render(request, 'Cajera/Ventas.html',context)




def ClienteRegistrado_DatosPropiedad(request):
    context = {}
    return render(request, 'ClienteRegistrado/DatosPropiedad.html',context)

def ClienteRegistrado_Inmuebles(request):
    context = {}
    return render(request, 'ClienteRegistrado/Inmuebles.html',context)

def ClienteRegistrado_Principal(request):
    context = {}
    return render(request, 'ClienteRegistrado/Principal.html',context)

def ClienteRegistrado_SolicitarCita(request):
    context = {}
    return render(request, 'ClienteRegistrado/SolicitarCita.html',context)






def EmpleadoMarketing_DatosPropiedad(request):
    context = {}
    return render(request, 'EmpleadoMarketing/DatosPropiedad.html',context)

def EmpleadoMarketing_Inmuebles(request):
    context = {}
    return render(request, 'EmpleadoMarketing/Inmuebles.html',context)

def EmpleadoMarketing_Principal(request):
    context = {}
    return render(request, 'EmpleadoMarketing/Principal.html',context)





def GerenteGeneral_DatosPropiedad(request):
    context = {}
    return render(request, 'GerenteGeneral/DatosPropiedad.html',context)

def GerenteGeneral_Inmuebles(request):
    context = {}
    return render(request, 'GerenteGeneral/Inmuebles.html',context)

def GerenteGeneral_Principal(request):
    context = {}
    return render(request, 'GerenteGeneral/Principal.html',context)

def GerenteGeneral_Reportes(request):
    context = {}
    return render(request, 'GerenteGeneral/Reportes.html',context)






def internauta_DatosPropiedad(request):
    context = {}
    return render(request, 'internauta/DatosPropiedad.html',context)

def internauta_Inmuebles(request):
    context = {}
    return render(request, 'internauta/Inmuebles.html',context)

def Principal(request):
    return render(request, 'Principal.html')

def internauta_register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='cliente')
            user.groups.add(group)
            messages.success(request, 'la carga ha sido exitosa ' + user.username)
            return redirect('login')
    else:
        form = CreateUserForm()

    return render(request,'internauta/register.html', {'form': form})



def JefaAdministracion_DatosPropiedad(request):
    context = {}
    return render(request, 'JefaAdministracion/DatosPropiedad.html',context)

def JefaAdministracion_Inmuebles(request):
    context = {}
    return render(request, 'JefaAdministracion/Inmuebles.html',context)

def JefaAdministracion_Principal(request):
    context = {}
    return render(request, 'JefaAdministracion/Principal.html',context)

def JefaAdministracion_Clientes(request):
    context = {}
    return render(request, 'JefaAdministracion/Clientes.html',context)

def JefaAdministracion_Reportes(request):
    context = {}
    return render(request,'JefaAdministracion/Reportes.html',context)

def JefaAdministracion_Transacciones(request):
    context = {}
    return render(request, 'JefaAdministracion/Transacciones.html',context)





def JefaComercializacion_DatosPropiedad(request):
    context = {}
    return render(request, 'JefaComercializacion/DatosPropiedad.html',context)

def JefaComercializacion_Inmuebles(request):
    context = {}
    return render(request, 'JefaComercializacion/Inmuebles.html',context)

def JefaComercializacion_Principal(request):
    context = {}
    return render(request, 'JefaComercializacion/Principal.html',context)

def JefaComercializacion_Clientes(request):
    context = {}
    return render(request, 'JefaComercializacion/Clientes.html',context)

def JefaComercializacion_Reportes(request):
    context = {}
    return render(request,'JefaComercializacion/Reportes.html',context)

def JefaComercializacion_Propiedades(request):
    context = {}
    return render(request, 'JefaComercializacion/Propiedades.html',context)

def JefaComercializacion_Actuales(request):
    context = {}
    return render(request, 'JefaComercializacion/Actuales.html',context)

def JefaComercializacion_Agenda(request):
    context = {}
    return render(request, 'JefaComercializacion/Agenda.html',context)

def JefaComercializacion_Antiguos(request):
    context = {}
    return render(request, 'JefaComercializacion/Antiguos.html',context)

def JefaComercializacion_Historico(request):
    context = {}
    return render(request, 'JefaComercializacion/Historico.html',context)

def JefaComercializacion_ClientesHistorico(request):
    context = {}
    return render(request,'JefaComercializacion/ClientesHistorico.html',context)

def JefaComercializacion_Vendidas(request):
    context = {}
    return render(request, 'JefaComercializacion/Vendidas.html',context)





def Secretaria_AceptarSolicitud(request):
    context = {}
    return render(request, 'Secretaria/AceptarSolicitud.html',context)

def Secretaria_Agenda(request):
    context = {}

    proximos_turnos = Turno.getProximosTurnos(1)
    context.setdefault("proximos_turnos", proximos_turnos)
    email_buscado = request.GET.get('email-buscar')
    telefono_buscado = request.GET.get('numero-buscar')
    fecha_buscada = str(request.GET.get('fecha-buscar')).replace('-', "")

    if email_buscado != '' and email_buscado is not None:
        try:
            cliente = Cliente.objects.get(email__iexact=email_buscado)
            context.setdefault("cliente", cliente)
            request.session['cliente'] = cliente.id
            context.setdefault("url", request.get_full_path())
        except:
            context.setdefault("cliente", "")

    if fecha_buscada != "None":
        if request.session['cliente']:
            cliente = Cliente.objects.get(pk=request.session['cliente'])
            context.setdefault("cliente", cliente)
        turnos_disponibles = Turno.getHorariosDisponibles(fecha_buscada)
        context.setdefault("turnos_disponibles", turnos_disponibles)
        context.setdefault("fecha_buscada", request.GET.get('fecha-buscar'))

    return render(request, 'Secretaria/Agenda.html', context)

def esFechaValida(fecha):
    fecha_hoy = int(str(datetime.today().strftime('%Y-%m-%d')).replace("-", ""))
    fecha = int(fecha.replace("/", ""))
    print(fecha_hoy, fecha, fecha_hoy > fecha)
    return fecha_hoy < fecha


def ProgramarCita(request):
    cliente = Cliente.objects.get(pk=request.session['cliente'])
    fecha_buscada = request.GET.get('fecha-buscar')

    proximos_turnos = Turno.getProximosTurnos(5)
    turnos_disponibles = []
    if fecha_buscada != "None":
        fecha = str(fecha_buscada).replace('-', "")
        turnos_disponibles = Turno.getHorariosDisponibles(fecha)

    if request.method == "POST":
        form = ProgramarCitaForm(request.POST)
        fecha = request.POST['dia']
        hora = request.POST['hora']
        agente = request.POST['agente']
        if form.is_valid() and Turno.estaDisponible(fecha, hora, agente) and esFechaValida(fecha):
            form.save()
            return redirect('Secretaria_Agenda')
        elif not esFechaValida(fecha):
            messages.error(request, "La fecha ingresada es menor a la actual.")
        elif not Turno.estaDisponible(fecha, hora, agente):
            messages.error(request, "Ese turno ya fue asignado.")
        else:
            messages.error(request, "Se produjo un error y no se completó la carga.")
    else:

        form = ProgramarCitaForm(initial={"cliente":cliente})
    return render(request, 'Secretaria/programar_cita.html', {'form': form, 'cliente':cliente, 'turnos_disponibles': turnos_disponibles, 'proximos_turnos': proximos_turnos, 'fecha_buscada': fecha_buscada})

def TurnosDados(request):
    context={}
    fecha_buscada = request.GET.get('fecha-buscar')
    context.setdefault("turnos", Turno.getTurnosDados(fecha_buscada))
    return render(request, 'Secretaria/turnosDados.html', context)

def AgendarCita(request):
    context = {}
    return render(request, 'Secretaria/agendarCita.html', context)

def Secretaria_CancelarCita(request):
    context = {}
    return render(request, 'Secretaria/CancelarCita.html',context)

def Secretaria_Clientes(request):
    context = {}
    return render(request, 'Secretaria/Clientes.html',context)

def Secretaria_DatosPropiedad(request):
    context = {}
    return render(request,'Secretaria/DatosPropiedad.html',context)

def Secretaria_Editar(request):
    context = {}
    return render(request, 'Secretaria/Editar.html',context)

def Secretaria_EditarCita(request):
    context = {}
    return render(request, 'Secretaria/EditarCita.html',context)

def Secretaria_Inmuebles(request):
    context = {}
    return render(request, 'Secretaria/Inmuebles.html',context)

def Secretaria_Solicitudes(request):
    context = {}
    return render(request, 'Secretaria/Solicitudes.html',context)
