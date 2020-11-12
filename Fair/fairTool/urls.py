from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tool/', views.RAtool.as_view(), name='tool'),
    path('maps/', views.HMap.as_view(), name= 'hmap'),
    path('about/', views.about, name = 'about'),
    path('dshbrd/', views.dashboard, name = 'dashboard')
]