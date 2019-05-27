from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name = 'index'),     #cuando no pones extension en url
    url(r'^productos/$',views.resultado, name = 'resultado'),
    url(r'^principal/$',views.principal, name = 'principal'),
    url(r'^sumar/$',views.sumar, name = 'sumar'),
    url(r'^listar/$',views.detalle, name = 'listar'),
]
