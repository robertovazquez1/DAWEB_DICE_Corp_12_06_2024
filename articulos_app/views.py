from django.shortcuts import render,redirect
from .models import Articulo

# Create your views here.
def index_Articulos(request):
    nArticulos=Articulo.objects.all()
    return render(request,'gestart.html',{'mArticulos':nArticulos})

def regisArticulos(request): 
    id=request.POST["txtid"]
    nom=request.POST["nom"]
    can=request.POST["can"]
    pre=request.POST["pre"]
    est=request.POST["est"]
    fec=request.POST["fecha"]
    colo=request.POST["col"]
    
    guarArticulo=Articulo.objects.create(
            id_articulo=id,
            cantidad_arti=can,
            nombre=nom,
            precio=pre,
            fecha_crea=fec,
            estado=est,
            color=colo,
    )
    return redirect("Articulos")

def selecart(request,id):
    cli=Articulo.objects.get(id_articulo=id)
    return render(request,'editarart.html',{"mArticulos":cli})

def editart(request):
    id=request.POST["txtid"]
    nom=request.POST["nom"]
    can=request.POST["can"]
    pre=request.POST["pre"]
    est=request.POST["est"]
    fec=request.POST["fecha"]
    colo=request.POST["col"]
    ins=Articulo.objects.get(id_articulo=id)
    ins.cantidad_arti=can
    ins.nombre=nom
    ins.precio=pre
    ins.fecha_crea=fec
    ins.estado=est
    ins.color=colo
    ins.save()
    return redirect('Articulos')

def borrarart(request,id):
    cli=Articulo.objects.get(id_articulo=id)
    cli.delete()
    return redirect('Articulos')