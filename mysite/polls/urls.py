from polls import views
from django.urls import path, include

urlpatterns = [
    path ('', views.index.as_view(), name = 'paquito'),
    path ('registro', views.register.as_view(), name = 'registrito'),
    path ('logueo', views.login.as_view(), name = 'logueadito'),
]