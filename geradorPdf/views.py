from django.shortcuts import render
from .models import Profile

def form(request):
    return render(request,'form.html')



