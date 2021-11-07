from django.shortcuts import render



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
    return render(request, 'EmpleadoMarketing/Principal',context)





def GerenteGeneral_DatosPropiedad(request):
    context = {}
    return render(request, 'GerenteGeneral/DatosPropiedad.html',context)

def GerenteGeneral_Inmuebles(request):
    context = {}
    return render(request, 'GerenteGeneral/Inmuebles.html',context)

def GerenteGeneral_Principal(request):
    context = {}
    return render(request, 'GerenteGeneral/Principal',context)

def GerenteGeneral_Reportes(request):
    context = {}
    return render(request, 'GerenteGeneral/Reportes.html',context)






def internauta_DatosPropiedad(request):
    context = {}
    return render(request, 'internauta/DatosPropiedad.html',context)

def internauta_Inmuebles(request):
    context = {}
    return render(request, 'internauta/Inmuebles.html',context)

def internauta_Principal(request):
    context = {}
    return render(request, 'internauta/Principal',context)

def internauta_login(request):
    context = {}
    return render(request, 'internauta/login.html',context)

def internauta_register(request):
    context = {}
    return render(request, 'internauta/register.html',context)



def JefaAdministracion_DatosPropiedad(request):
    context = {}
    return render(request, 'JefaAdministracion/DatosPropiedad.html',context)

def JefaAdministracion_Inmuebles(request):
    context = {}
    return render(request, 'JefaAdministracion/Inmuebles.html',context)

def JefaAdministracion_Principal(request):
    context = {}
    return render(request, 'JefaAdministracion/Principal',context)

def JefaAdministracion_login(request):
    context = {}
    return render(request, 'JefaAdministracion/Clientes.html',context)

def JefaAdministracion_Reportes(request):
    context = {}
    return render(request,'JefaAdministracion/Reportes.html',context)

def JefaAdministracion_Transacciones(request):
    context = {}
    return render(request, 'JefaAdministracion/Transacciones.html',context)