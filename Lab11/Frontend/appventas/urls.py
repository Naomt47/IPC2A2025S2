from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/carga', views.carga, name='carga'),
    path('cargaxml/', views.cargarXML, name='cargaxml'),
    path('cargarxml/', views.procesarXML, name='cargarxml'), #/venta/cargar
    path('closemessages1/', views.cerrarMensajesCargarXML, name='closemessages1'),
    path('ventas/', views.verTablaVentas, name='ventas'),
    path('ventaspormes/', views.verVentasMensuales, name='pormes'),
    path('verpdf/', views.verPdf, name='verpdf')
]
