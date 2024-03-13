from django.shortcuts import render
from django.http import HttpResponse
from . models import Weapon


# Create your views here.


#def index2(request):
#    return HttpResponse("<H1> Welcome to my Page <H1/>")

''' 
def index2(request):
    return HttpResponse("Hello World!")

'''


def index(request):
    context={
        "weapons": Weapon.objects.all()
    }
    return render(request, "weapon/index.html", context) # using class weapon from models that i created before

