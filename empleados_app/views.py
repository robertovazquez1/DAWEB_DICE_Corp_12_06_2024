from django.shortcuts import render,redirect
from .models import Empleado
# Create your views here.

def index_Empleados(request):
    nEmpleados=Empleado.objects.all()
    return render(request,'gestEmp.html',{'lamp':nEmpleados})

def regisEmpleados(request): 
    id=request.POST["txtid"]
    nombre=request.POST["txtnom"]
    ape=request.POST["ape"]
    cel=request.POST["num"]
    gen=request.POST["gen"]
    suel=request.POST["sue"]
    pues=request.POST["pue"]
    
    guarEmpleado=Empleado.objects.create(
            id_empleado=id,
            nombre=nombre,
            apellido=ape,
            salario=suel,
            genero=gen,
            telefono=cel,
            puesto=pues,
    )
    return redirect("Empleados")

def selecEmp(request,id):
    cli=Empleado.objects.get(id_empleado=id)
    return render(request,'editarEmp.html',{"mEmpleados":cli})

def editEmp(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnom"]
    ape=request.POST["ape"]
    cel=request.POST["num"]
    gen=request.POST["gen"]
    suel=request.POST["sue"]
    pues=request.POST["pue"]
    emp=Empleado.objects.get(id_empleado=id)
    emp.nombre=nombre
    emp.apellido=ape
    emp.salario=suel
    emp.genero=gen
    emp.telefono=cel
    emp.puesto=pues
    emp.save()
    return redirect('Empleados')

def borraEmp(request,id):
    cli=Empleado.objects.get(id_empleado=id)
    cli.delete()
    return redirect('Empleados')