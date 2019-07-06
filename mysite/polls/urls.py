from polls import views
from django.urls import path, include

urlpatterns = [
    path ('', views.index.as_view(), name = 'paquito'),
    path ('registro', views.register.as_view(), name = 'registrito'),
    path ('logueo', views.loginIt.as_view(), name = 'logueadito'),
    path ('deslogueo', views.logout_view, name = 'deslogueadito'),
    path ('tablaUser', views.tabladeUsuarios.as_view(), name = 'usuarito'),
    path ('usuario/<int:id>', views.editarUsuario.as_view(), name = 'editadito'),
    path ('imp3D', views.registerImpresion.as_view(), name = "impresito"),

]