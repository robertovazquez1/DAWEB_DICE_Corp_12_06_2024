from django.shortcuts import render,redirect
from .models import Local

# Create your views here.
def index_Local(request):
    nLocal=Local.objects.all()
    return render(request,'gestLoc.html',{'lamp':nLocal})

def regisLocals(request): 
    id=request.POST["txtid"]
    ubi=request.POST["ubi"]
    fun=request.POST["afu"]
    hor=request.POST["hor"]
    tam=request.POST["tam"]
    due=request.POST["due"]
    emp=request.POST["emp"]
    
    guarLocal=Local.objects.create(
            id_local=id,
            ubicacion=ubi,
            anos_funcio=fun,
            horario=hor,
            tamano=tam,
            dueno=due,
            empleados_total=emp,
    )
    return redirect("Local")

def selecLoc(request,id):
    suc=Local.objects.get(id_local=id)
    return render(request,'editarLoc.html',{"mLocals":suc})

def editLoc(request):
    id=request.POST["txtid"]
    ubi=request.POST["ubi"]
    fun=request.POST["afu"]
    hor=request.POST["hor"]
    tam=request.POST["tam"]
    due=request.POST["due"]
    emp=request.POST["emp"]
    suc=Local.objects.get(id_local=id)
    suc.ubicacion=ubi
    suc.anos_funcio=fun
    suc.horario=hor
    suc.tamano=tam
    suc.dueno=due
    suc.empleados_total=emp
    suc.save()
    return redirect('Local')

def borraLoc(request,id):
    suc=Local.objects.get(id_local=id)
    suc.delete()
    return redirect('Local')