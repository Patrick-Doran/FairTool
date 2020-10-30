from django.shortcuts import render
from django.http import HttpResponse
from .models import Input


#this is our back end

def index(request):
    context = {'fuck this':1}
    return render(request, 'fairTool/index.html', context)