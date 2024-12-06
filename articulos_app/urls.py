from django.urls import path
from articulos_app import views

urlpatterns = [
    path('Articulos',views.index_Articulos,name='Articulos'),
    path('registrar_Articulos/',views.regisArticulos,name='registrar_Articulos'),
    path('seleccionar_articulos/<id>',views.selecart,name="seleccionar_articulos"),
    path('editar_articulos/',views.editart,name="editar_articulos"),
    path('borrar_articulos/<id>',views.borrarart,name="borrar_articulos"),
]