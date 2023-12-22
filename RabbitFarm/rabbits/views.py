# rabbits/views.py
from django.shortcuts import render
from .models import Rabbit
from django.shortcuts import render, get_object_or_404

def rabbit_list(request):
    rabbits = Rabbit.objects.all()
    return render(request, 'rabbits/rabbit_list.html', {'rabbits': rabbits})

def rabbit_detail(request, pk):
    rabbit = get_object_or_404(Rabbit, pk=pk)
    return render(request, 'rabbits/rabbit_detail.html', {'rabbit': rabbit})