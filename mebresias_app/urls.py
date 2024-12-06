from django.urls import path
from mebresias_app import views

urlpatterns = [
    path('Membresia',views.index_Membresia,name='Membresia'),
    path('registrar_Membresias/',views.regisMembresias,name='registar_Ventas'),
    path('seleccionar_Membresias/<id>',views.selecVen,name="seleccionar_Ventas"),
    path('editar_Membresias/',views.editVen,name="editar_Ventas"),
    path('borrar_Membresias/<id>',views.borraVen,name="borrar_Ventas"),
]