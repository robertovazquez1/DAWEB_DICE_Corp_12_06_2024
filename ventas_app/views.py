from django.shortcuts import render,redirect
from .models import Venta

# Create your views here.
def index_Venta(request):
    nVenta=Venta.objects.all()
    return render(request,'gestVen.html',{'lamp':nVenta})

def regisVentas(request): 
    id=request.POST["txtid"]
    emp=request.POST["ide"]
    cli=request.POST["idc"]
    art=request.POST["ida"]
    loc=request.POST["idl"]
    cac=request.POST["cac"]
    mp=request.POST["mp"]
    total=request.POST["tot"]
    
    guarVenta=Venta.objects.create(
            id_venta=id,
            id_empleado=emp,
            id_cliente=cli,
            id_articulo=art,
            id_local=loc,
            cantidad_compra=cac,
            metodo_pago=mp,
            total=total
    )
    return redirect("Venta")

def selecVen(request,id):
    suc=Venta.objects.get(id_venta=id)
    return render(request,'editarVen.html',{"mVentas":suc})

def editVen(request):
    id=request.POST["txtid"]
    emp=request.POST["ide"]
    cli=request.POST["idc"]
    art=request.POST["ida"]
    loc=request.POST["idl"]
    cac=request.POST["cac"]
    mp=request.POST["mp"]
    total=request.POST["tot"]
    ven=Venta.objects.get(id_venta=id)
    ven.id_empleado=emp
    ven.id_cliente=cli
    ven.id_articulo=art
    ven.id_local=loc
    ven.cantidad_compra=cac
    ven.metodo_pago=mp
    ven.total=total
    ven.save()
    return redirect('Venta')

def borraVen(request,id):
    suc=Venta.objects.get(id_venta=id)
    suc.delete()
    return redirect('Venta')