from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='PHPapp/php_home_page.html'), name='home-page'),
   
]