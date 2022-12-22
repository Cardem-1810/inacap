from django.shortcuts import render, redirect
from Templates.models import Reservas
from .serializers import ReservasSerializer
from Templates.forms import FormReservas
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


# Create your views here.

def index(request):
    return render(request, 'index.html')

def reservas(request):
    res = Reservas.objects.all()
    data = {'reservas': res}
    return render(request, 'reservas.html', data)

def agregarreserva(request):
    form = FormReservas()
    if request.method == 'POST':
        form = FormReservas(request.POST)
        if form.is_valid():
            form.save()
        return index(request)

    data = {'form' : form}
    return render(request, 'agregarreserva.html', data)        

def eliminarreserva(request, id):
    pro = Reservas.objects.get(id = id)
    pro.delete()

    return redirect('/reservas')

def actualizarreserva(request, id):
    res = Reservas.objects.get(id = id)
    form = FormReservas(instance=res)
    if request.method == 'POST':
        form = FormReservas(request.POST, instance=res)
        if form.is_valid():
            form.save()
        return index(request)

    data = {'form' : form}
    return render(request, 'agregarreserva.html', data)

    # API REST

class ReservasLista(APIView):
    def get(self, request):
        estu = Reservas.objects.all()
        serial = ReservasSerializer(estu, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = ReservasSerializer(data = request.data)
        if serial.is_valid():
            serial.save
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservasDetalle(APIView):
    def get_object(self, pk):
        try:
            return Reservas.objects.get(id=pk)
        except Reservas.DoesNotExist:
            return Http404

    def get(self, request, pk):
        estu = self.get_object(pk)
        serial = ReservasSerializer(estu)
        return Response(serial.data)

    def put (self, request, pk):
        estu = self.get_object(pk)
        serial = ReservasSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        estu = self.get_object(pk)
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)