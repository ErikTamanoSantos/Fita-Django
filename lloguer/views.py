from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from lloguer.models import *

# Create your views here.
def main(request):
    automobils = Automobil.objects.all()
    return render(request, 'index.html', {'automobils': automobils})