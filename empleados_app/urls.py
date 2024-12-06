from django.urls import path
from empleados_app import views

urlpatterns = [
    path('Empleados',views.index_Empleados,name='Empleados'),
    path('registrar_Empleados/',views.regisEmpleados,name='registrar_Empleados'),
    path('seleccionar_Empleado/<id>',views.selecEmp,name="seleccionar_Empleado"),
    path('editar_Empleado/',views.editEmp,name="editar_Empleado"),
    path('borrar_Empleado/<id>',views.borraEmp,name="borrar_Empleado"),
]