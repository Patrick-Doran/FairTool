from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Input


#this is our back end

def index(request):
    print("rendered index")
    return render(request, 'fairTool/index.html')

class RAtool(View):
    def get(self, request):
        return render(request, 'fairTool/tool.html')

class HMap(View):
    def get(self, request):
        return render(request, 'fairTool/heatmap.html')