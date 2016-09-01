__author__ = 'mrk2'
from  django.db.models import QuerySet, Q
from reservaciones.models import Reservacion


class CarQS(QuerySet):

    def todos_disponibles(self, fecha_inicio, fecha_termino ):
        reservaciones = Reservacion.objects.from_to()


class ReservacionesQS(QuerySet):
    def from_to(self, fecha_inicio, fecha_termino):
        return self.filter(
            Q(fecha_inicio__range=(fecha_inicio, fecha_termino)) |
            Q(fecha_termino__range=(fecha_inicio, fecha_termino))
        )

    def car_model(self, car_model_pk):
        return self.filter()