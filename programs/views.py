from django.shortcuts import render
from .models import Program

def program_list(request):
    programs = Program.objects.all()
    return render(request, 'programs/list.html', {'programs': programs})

def home(request):
    return render(request, 'base.html')

