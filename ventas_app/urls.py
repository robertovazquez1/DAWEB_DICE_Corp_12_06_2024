from django.urls import path
from ventas_app import views

urlpatterns = [
    path('Venta',views.index_Venta,name='Venta'),
    path('registar_Ventas/',views.regisVentas,name='registar_Ventas'),
    path('seleccionar_Ventas/<id>',views.selecVen,name="seleccionar_Ventas"),
    path('editar_Ventas/',views.editVen,name="editar_Ventas"),
    path('borrar_Ventas/<id>',views.borraVen,name="borrar_Ventas"),
]