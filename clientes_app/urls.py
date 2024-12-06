from django.urls import path
from clientes_app import views

urlpatterns = [
    path('clientes',views.index_Clientes,name='clientes'),
    path('registraClientes/',views.regisClientes,name='registraClientes'),
    path('seleccionar_Cliente/<id>',views.selecCli,name="selecCli"),
    path('editar_Clientes/',views.editCli,name="editCli"),
    path('borrar_Clientes/<id>',views.borrarCli,name="borrarCli"),
]
