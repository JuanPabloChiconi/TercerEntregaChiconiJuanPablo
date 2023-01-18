

# Create your views here.
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from AppCoder.forms import DatosPersonalesFormulario, SensoresFormulario, UsuarioFormulario
from AppCoder.models import DatosPersonales, Sensores, Usuario

#parte mia

#parte mia

# Create your views here.
"""

    
"""


#parte mia
    
    
from django.views.generic.detail import DetailView

def inicio(request):

    return render(request, "AppCoder/inicio.html")
  


class DatosPersonalesDetalle(DetailView):

    model = DatosPersonales
    template_name = "AppCoder/DatosPersonales.html"
    
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


from django.views.generic.edit import UpdateView

class DatosPersonalesUpdate(UpdateView):

    model = DatosPersonales
    success_url = "/AppCoder/DatosPersonales.html"
    fields = ['direccion', 'telefono', 'email']

"""



from django.views.generic import ListView

class SensoresList(ListView):

    model = Sensores
    template_name = "AppCoder/Sensores_list.html"


from django.views.generic.detail import DetailView


class SensoresDetalle(DetailView):

    model = Sensores
    template_name = "AppCoder/Sensores_detalle.html"
    
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class CursoCreacion(CreateView):

    model = Sensores
    success_url = "/AppCoder/Sensores/list"
    fields = ['identificacion', 'modelo', 'valor']

from django.views.generic.edit import UpdateView

class SensoresUpdate(UpdateView):

    model = Sensores
    success_url = "/AppCoder/Sensores/list"
    fields = ['identificacion', 'modelo', 'valor']


from django.views.generic.edit import DeleteView
class SensoresDelete(DeleteView):

    model = Sensores
    success_url = "/AppCoder/Sensores/list"

"""





"""
def buscar(request):

      if  request.GET("modelo"):

	      #respuesta = f"Estoy buscando el modelo nro: {request.GET['modelo'] }" 
            modelo = request.GET("modelo")
            sensores = Sensores.objects.filter(modelo__icontains=modelo)

            return render(request, "AppCoder/inicio.html", {"Sensores:":sensores,"Modelo":modelo})
            

      else: 
            respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
            return HttpResponse(respuesta)  
"""

def buscar(request):
      modelo =request.GET["modelo"]
      if modelo != "" :
            #sensores = Sensores.objects.filter(modelo)
            #respuesta = ("Sensores:", modelo)
            
            #return HttpResponse(respuesta)
            sensores = Sensores.objects.filter(modelo__icontains=modelo)
            return render(request, "AppCoder/inicio.html", {"sensoresmodelo":sensores, "Modelo":modelo})
      else: 
            respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
            return HttpResponse(respuesta)




### INICIO SENSORES

def leerSensores(request):

      sensores = Sensores.objects.all() #trae todos los sensores

      contexto= {"sensores":sensores} 

      return render(request, "AppCoder/leerSensores.html",contexto)



    
def eliminarSensor(request, sensor_identificacion):

    sensor = Sensores.objects.get(identificacion=sensor_identificacion)
    sensor.delete()
    # vuelvo al menú
    sensor2 = Sensores.objects.all()  # trae todos los sensores
    contexto = {"sensores": sensor2}
    return render(request, "AppCoder/leerSensores.html", contexto)


    
 
  

###   CARGA DE DATOS DE SENSORES   


from AppCoder.forms import SensoresFormulario      
def agregarSensores(request):
      if request.method == 'POST':
            miFormulario = SensoresFormulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacionnueva = miFormulario.cleaned_data
                  sensoresactualizados = Sensores(identificacion=informacionnueva['identificacion'], modelo=informacionnueva['modelo'],valor=
                   informacionnueva['valor'])
                  sensoresactualizados.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= SensoresFormulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/sensores.html", {"miFormulario":miFormulario})
  


def editarSensor(request, sensor_identificacion):

    # Recibe el nombre del sensor que vamos a modificar
    sensor= Sensores.objects.get(identificacion=sensor_identificacion)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = SensoresFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            sensor.identificacion = informacion['identificacion']
            sensor.modelo = informacion['modelo']
            sensor.valor = informacion['valor']
    

            sensor.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = SensoresFormulario(initial={'identificacion':sensor.identificacion, 'modelo':sensor.modelo,
                                                   'valor':sensor.valor})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarSensor.html", {"miFormulario": miFormulario, "identificacion": sensor_identificacion})

### FIN SENSORES

### INICIO USUARIOS

def leerUsuarios(request):

      usuarios = Usuario.objects.all() #trae todos los sensores

      contexto= {"usuarios":usuarios} 

      return render(request, "AppCoder/leerUsuarios.html",contexto)



    
def eliminarUsuario(request, usuario_nombre):

    usuarios = Usuario.objects.get(nombre=usuario_nombre)
    usuarios.delete()
    # vuelvo al menú
    usuarios2 = Usuario.objects.all()  # trae todos los sensores
    contexto = {"usuario": usuarios2}
    return render(request, "AppCoder/leerUsuarios.html", contexto)

   

###   CARGA DE DATOS DE USUARIOS      
from AppCoder.forms import UsuarioFormulario      
def agregarUsuario(request):
      if request.method == 'POST':
            miFormulario = UsuarioFormulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacionnueva = miFormulario.cleaned_data
                  usuariosactualizados = Usuario(nombre=informacionnueva['nombre'], apellido=informacionnueva['apellido'],dni=
                   informacionnueva['dni'])
                  usuariosactualizados.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= UsuarioFormulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/usuarios.html", {"miFormulario":miFormulario})
  

def editarUsuario(request, usuario_nombre):

    # Recibe el nombre del usuario que vamos a modificar
    usuario= Usuario.objects.get(nombre=usuario_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = UsuarioFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            usuario.nombre = informacion['nombre']
            usuario.apellido = informacion['apellido']
            usuario.dni = informacion['dni']
    

            usuario.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = UsuarioFormulario(initial={'nombre':usuario.nombre, 'apellido':usuario.apellido,
                                                   'dni':usuario.dni})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarUsuario.html", {"miFormulario": miFormulario, "identificacion": usuario_nombre})

### FIN USUARIOS


### INICIO DATOS PERSONALES



def leerDatosPersonales(request):

      datospersonales = DatosPersonales.objects.all() #trae todos los sensores

      contexto= {"datospersonales":datospersonales} 

      return render(request, "AppCoder/leerDatosPersonales.html",contexto)



    
def eliminarDatosPersonales(request, datospersonales_direccion):

    datospersonales = DatosPersonales.objects.get(nombre=datospersonales_direccion)
    datospersonales.delete()
    # vuelvo al menú
    datospersonales2 = DatosPersonales.objects.all()  # trae todos los sensores
    contexto = {"datospersonales": datospersonales2}
    return render(request, "AppCoder/leerDatosPersonales.html", contexto)

  

###   CARGA DE DATOS DE USUARIOS      
from AppCoder.forms import DatosPersonalesFormulario      
def agregarDatosPersonales(request):
      if request.method == 'POST':
            miFormulario = DatosPersonalesFormulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacionnueva = miFormulario.cleaned_data
                  datospersonalesactualizados = DatosPersonales(direccion=informacionnueva['direccion'], telefono=informacionnueva['telefono'],email=
                   informacionnueva['email'])
                  datospersonalesactualizados.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= DatosPersonalesFormulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/datospersonales.html", {"miFormulario":miFormulario})
  

def editarDatosPersonales(request, datospersonales_direccion):

    # Recibe el nombre del sensor que vamos a modificar
    datospersonales= DatosPersonales.objects.get(direccion=datospersonales_direccion)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = DatosPersonalesFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            datospersonales.direccion = informacion['direccion']
            datospersonales.telefono = informacion['telefono']
            datospersonales.email = informacion['email']
    

            datospersonales.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = DatosPersonalesFormulario(initial={'direccion':datospersonales.direccion, 'telefono':datospersonales.telefono,
                                                   'email':datospersonales.email})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarDatosPersonales.html", {"miFormulario": miFormulario, "identificacion": datospersonales_direccion})





### FIN DATOS PERSONALES


