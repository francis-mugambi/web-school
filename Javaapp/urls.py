from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='basicpages/comming_soon.html'), name='home-page'),
   
]