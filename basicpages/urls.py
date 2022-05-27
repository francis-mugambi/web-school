from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_view.as_view(), name='home-page'),
    path('about/', views.about_view.as_view(), name='about-page'),
    path('contact/', views.contact_view, name='contact-page'),
    path('how-to-enable-touchpad/', TemplateView.as_view(template_name='basicpages/touchpad_enable.html'), name='touchpad-page'),
]