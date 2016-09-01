from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Carro
from reservaciones.models import Reservacion
from reservaciones.forms import ClienteForm, ReservacionForm, TarjetaForm, ReservacionPanel
from django.db.models import Avg
# Create your views here.

def index(request):
    form = ReservacionPanel()
    carros = Carro.objects.filter(disponibilidad=True)
    if request.method == 'POST':

        form = ReservacionPanel(request.POST)
        # fecha = form.cleaned_data['fecha_inicio']
        fecha = request.POST.get('fecha_inicio', '')
        if Reservacion.objects.get(fecha_inicio=fecha).exists():
            a = Reservacion.objects.all().exclude(fecha_inicio=fecha)
            context= {
                'a':a,
                'carros': carros,
                'form': form,
            }
            return render(request, 'index.html', context)

        else:
            return redirect('https://www.youtube.com/watch?v=lMi4QmNHSDg&list=LLEjjD9euB_Db-tGF33PgfUg&index=30')

    context = {
        'carros': carros,
        'form': form,
    }
    return render(request, 'index.html', context)

def miperfil(request):
    usuario = request.user
    mis_reservaciones = Reservacion.objects.filter(cliente=usuario)
    return render(request, 'perfil/mi_perfil.html', {'mi_reservacion': mis_reservaciones})

def detalle_carro(request, object_id=None):
    carro = get_object_or_404(Carro, id=object_id)
    formreservacion = ReservacionForm()
    if request.method == 'POST':
        reservacionf = ReservacionForm(request.POST)
        # if request.user.is_anonymous:
        #     return HttpResponse("Desves de loguearte")
        # else:
        if reservacionf.is_valid():
            usuario = request.user
            # car = reservacionf.cleaned_data['carro']
            # sacarc = Carro.objects.get(pk=car)
            Reservacion.objects.create(
                cliente=usuario,
                fecha_inicio=reservacionf.cleaned_data['fecha_inicio'] ,
                fecha_termino=reservacionf.cleaned_data['fecha_termino'] ,
                carro=reservacionf.cleaned_data['carro'],
                )
        return redirect('datos_tarjeta')

    return render(request, 'detalle_carro.html', {'carro':carro,
                                                  'formres': formreservacion})
def datos_tarjeta(request):
    if request.method == 'POST':
        formTarjeta = TarjetaForm(request.POST)
        if formTarjeta.is_valid():
            formTarjet = formTarjeta.save(commit=False)
            formTarjet.usuario = request.user
            formTarjet.save()
            redirect('pago_realizado')

    usuario = request.user
    reserva = Reservacion.objects.filter(cliente=usuario).last()
    rnicio = reserva.fecha_inicio
    rfinal = reserva.fecha_termino
    dayt = abs((rnicio-rfinal).days)
    rcarrop_day = reserva.carro.precio_por_dia
    total = dayt * rcarrop_day
    formTarjeta = TarjetaForm()
    return render(request, 'pago/pago_tarjeta.html', {'reserva': reserva,
                                                     'dayst': dayt,
                                                      'rcarrop_day': rcarrop_day,
                                                      'total': total,
                                                      'formTarjeta':formTarjeta})


def pago_realizado(request):
    return render(request, 'pago/pago-realizado.html')

def automoviles(request):
    automoviles = Carro.objects.filter(categoria__nombre='Automovil')
    return render(request, 'categorias/automoviles.html', {'carros': automoviles,})

def pick_up(request):
    automoviles = Carro.objects.filter(categoria__nombre='Camioneta Pickup')
    return render(request, 'categorias/pick_up.html', {'carros': automoviles,})

def terminosCondiciones(request):
    return render(request, 'info/terminosCondiciones.html')

def preguntas(request):
    return render(request, 'info/preguntas.html')