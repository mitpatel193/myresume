from django.shortcuts import render,redirect
from .models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

