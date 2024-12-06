from django.shortcuts import render,redirect
from .models import Membresia

# Create your views here.
def index_Membresia(request):
    nMembresia=Membresia.objects.all()
    return render(request,'gestmem.html',{'lamp':nMembresia})

def regisMembresias(request): 
    id=request.POST["txtid"]
    nom=request.POST["nom"]
    can=request.POST["can"]
    tie=request.POST["tie"]
    pre=request.POST["pre"]
    des=request.POST["des"]
    col=request.POST["col"]
    
    guarMembresia=Membresia.objects.create(
            id_membresia=id,
            nombre=nom,
            cantidad=can,
            tiempo_vigen=tie,
            precio_membre=pre,
            descuento=des,
            color=col,
    )
    return redirect("Membresia")

def selecVen(request,id):
    suc=Membresia.objects.get(id_membresia=id)
    return render(request,'editarmem.html',{"mMembresias":suc})

def editVen(request):
    id=request.POST["txtid"]
    nom=request.POST["nom"]
    can=request.POST["can"]
    tie=request.POST["tie"]
    pre=request.POST["pre"]
    des=request.POST["des"]
    col=request.POST["col"]
    ven=Membresia.objects.get(id_membresia=id)
        
    ven.nombre=nom
    ven.cantidad=can
    ven.tiempo_vigen=tie
    ven.precio_membre=pre
    ven.descuento=des
    ven.color=col
    ven.save()
    return redirect('Membresia')

def borraVen(request,id):
    suc=Membresia.objects.get(id_membresia=id)
    suc.delete()
    return redirect('Membresia')