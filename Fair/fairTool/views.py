from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Input


#this is our back end

def index(request):
    print("rendered index")
    return render(request, 'fairTool/index.html')

def about(request):
    return render(request, 'fairTool/about.html')

def dashboard(request):
    return render(request, 'fairTool/dshbrd.html')

class RAtool(View):
    def get(self, request):
        return render(request, 'fairTool/tool.html')

    def post(self, request):
        return render(request,'fairTool/tool.html')

class HMap(View):
    def get(self, request):
        return render(request, 'fairTool/heatmap.html')