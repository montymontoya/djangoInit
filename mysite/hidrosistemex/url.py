from hidrosistemex import views
from django.urls import path, include

urlpatterns = [
    path ('temperatura', views.temperatura.as_view(), name = 'temperatura_'),
    path ('particulas', views.particulas.as_view(), name = 'particulas_'),
    path ('azufre', views.azufre.as_view(), name = 'azufre_'),
    path ('isobutileno', views.isobutileno.as_view(), name = 'isobutileno_'),
    path ('diocarbono', views.diocarbono.as_view(), name = 'diocarbono_'),
    path ('monocarbono', views.monocarbono.as_view(), name = 'monocarbono_'),
    path ('ozono', views.ozono.as_view(), name = 'ozono_'),
    path ('dionitro', views.dionitro.as_view(), name = 'dionitro_'),
    path ('nitrico', views.nitrico.as_view(), name = 'nitrico_'),
    path ('humedad', views.humedad.as_view(), name = 'humedad_'),
]