from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Widgets

def home(request):
    if request.method == 'POST':
        test = Widgets.objects.create(
            description = request.POST['description'],
            quantity = request.POST['quantity']
        )
    incoming = Widgets.objects.all()
    total = 0
    for i in incoming:
        total += i.quantity
    return render(request, 'wacky-widgets.html', {'incoming': incoming, 'total': total})

def delete(request, wid_id):
    removing = Widgets.objects.get(id=wid_id)
    removing.delete()
    return redirect('/')

