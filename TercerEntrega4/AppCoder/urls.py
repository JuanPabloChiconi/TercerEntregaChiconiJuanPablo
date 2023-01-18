from django.urls import path

from AppCoder import views


urlpatterns = [
    

    #path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    #path('cursos', views.cursos, name="Cursos"),
    #path('profesores', views.profesores, name="Profesores"),
    #path('estudiantes', views.estudiantes, name="Estudiantes"),
    #path('entregables', views.entregables, name="Entregables"),
  
    
    path('sensores', views.agregarSensores, name="Sensores"),
    path('usuarios', views.agregarUsuario, name="Usuarios"),
    path('datospersonales', views.agregarDatosPersonales, name="DatosPersonales"),
    path('eliminarsensor/<sensor_identificacion>/', views.eliminarSensor, name="eliminarSensor"),
    path('leerSensores', views.leerSensores, name="leerSensores"),
    path('buscar/', views.buscar),
    path('editarSensor/<sensor_identificacion>/', views.editarSensor, name="editarSensor"),

    path('eliminarusuarios/<usuario_nombre>/', views.eliminarUsuario, name="eliminarUsuario"),
    path('leerUsuarios', views.leerUsuarios, name="leerUsuarios"),
    path('editarUsuario/<usuario_nombre>/', views.editarUsuario, name="editarUsuario"),

    path('eliminarDatosPersonales/<datospersonales_direccion>/', views.eliminarDatosPersonales, name="eliminarDatosPersonales"),
    path('leerDatosPersonales', views.leerDatosPersonales, name="leerDatosPersonales"),
    path('editarDatosPersonales/<datospersonales_direccion>/', views.editarDatosPersonales, name="editarDatosPersonales"),



    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    
    
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    #path('buscar/', views.buscar),
    #path('leerProfesores', views.leerProfesores, name = "LeerProfesores"),
    #path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    #path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),
    
    #path('curso/list', views.CursoList.as_view(), name='List'),
    #path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    #path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    #path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    #path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    
    path(r'^editar/(?P<pk>\d+)$', views.DatosPersonalesUpdate.as_view(), name='Edit'),
    path(r'^refrescar/(?P<pk>\d+)$', views.DatosPersonalesDetalle.as_view(), name='Refrescar'),
    
]

