from django.shortcuts import render,redirect
from .models import Cliente

# Create your views here.
def index_Clientes(request):
    nclientes=Cliente.objects.all()
    return render(request,'gestCliente.html',{'mclientes':nclientes})

def regisClientes(request): 
    id=request.POST["txtid"]
    fecha=request.POST["fecen"]
    tiem=request.POST["tiempo"]
    com=request.POST["com"]
    mem=request.POST["idm"]
    meto=request.POST["mecom"]
    cali=request.POST["cali"]
    
    guarCliente=Cliente.objects.create(
            id_cliente=id,
            fecha_entrada=fecha,
            tiempo_local=tiem,
            compra=com,
            id_membresia=mem,
            metodo_pago=meto,
            calificacion_dada=cali
    )
    return redirect("clientes")

def selecCli(request,id):
    cli=Cliente.objects.get(id_cliente=id)
    return render(request,'editarCli.html',{"mclientes":cli})

def editCli(request):
    id=request.POST["txtid"]
    fecha=request.POST["fecen"]
    tiem=request.POST["tiempo"]
    com=request.POST["com"]
    mem=request.POST["idm"]
    meto=request.POST["mecom"]
    cali=request.POST["cali"]
    cli=Cliente.objects.get(id_cliente=id)
    cli.fecha_entrada=fecha
    cli.tiempo_local=tiem
    cli.compra=com
    cli.id_membresia=mem
    cli.metodo_pago=meto
    cli.calificacion_dada=cali
    cli.save()
    return redirect('clientes')

def borrarCli(request,id):
    cli=Cliente.objects.get(id_cliente=id)
    cli.delete()
    return redirect('clientes')