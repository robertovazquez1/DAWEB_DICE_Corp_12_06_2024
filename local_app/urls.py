from django.urls import path
from local_app import views

urlpatterns = [
    path('Local',views.index_Local,name='Local'),
    path('registrar_Local/',views.regisLocals,name='registrar_Local'),
    path('seleccionar_Local/<id>',views.selecLoc,name="seleccionar_Local"),
    path('editar_local/',views.editLoc,name="editar_local"),
    path('borrar_local/<id>',views.borraLoc,name="borrar_local"),
] 