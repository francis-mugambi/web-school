from django.contrib import admin
from django.urls import path
from .import views
from django.views.generic import TemplateView
from django.urls import path


app_name =' articles'
urlpatterns = [
    path('how-to-articles/', views.how_to_articles_view.as_view(), name='how-to-page'),
    path('article/<str:str>', views.article_view, name='article-page'),
    path('test/', TemplateView.as_view(template_name="articles/home_article_page.html")),

]