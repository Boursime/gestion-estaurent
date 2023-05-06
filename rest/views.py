from django.shortcuts import render
from .models import Menu, Plate
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    ty = Menu.objects.all()
    return render(request,'home.html', {
        'ty' :ty,
    })

def detail(request, pk):
    it = get_object_or_404(Plate, pk=pk)
    ty = get_object_or_404(Menu, pk=pk)
    return render(request,'plats.html', {
        'it' :it,
        'ty' :ty,
    })

def detail_d(request, pk):
    it = get_object_or_404(Plate, pk=pk)
    return render(request,'pl_det.html', {
        'it' :it,
    })

    

def plats(request):
    return render(request,'plats.html')

def ambiance(request):
    return render(request,'ambiance.html')