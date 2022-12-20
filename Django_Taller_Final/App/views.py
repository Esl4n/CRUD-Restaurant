from django.shortcuts import render,redirect
from .models import Reserva
# Create your views here.
def Inicio (request):
    return render(request, 'App/index.html')


def reserva(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        cantidadPersonas = request.POST.get('personas')
        estado = request.POST.get('estado')
        observacion = request.POST.get('observacion')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        r = Reserva.objects.create(
            nombre = nombre,
            apellido = apellido,
            telefono = telefono,
            cantidadPersonas = cantidadPersonas,
            estado = estado,
            observacion = observacion,
            fecha= fecha,
            hora =hora,
        )
        r.save()
        return redirect("/listado")
    elif request.method == 'GET':
        return render(request, 'App/Reserva.html')



def Lista(request):
    r = Reserva.objects.all()
    data ={'reserva':r}
    return render(request, 'App/listado.html',data)


def Delete(request,id):
    r = Reserva.objects.get(id =id)
    r.delete()
    return redirect('/listado')


def Modificar(request, id):
    if request.method == 'POST':
        id = request.POST.get('id')
        r = Reserva.objects.get(id=id)
        r.nombre = request.POST.get('nombre')
        r.apellido = request.POST.get('apellido')
        r.telefono = request.POST.get('telefono')
        r.cantidadPersonas = request.POST.get('personas')
        r.estado = request.POST.get('estado')
        r.observacion = request.POST.get('observacion')
        r.fecha = request.POST.get('fecha')
        r.hora = request.POST.get('hora')
        r.save()
        return redirect('/listado/')
    elif request.method == 'GET':
        r = Reserva.objects.get(id=id)
        data = {'reserva':r}
        return render(request, 'App/modificar.html', data)
