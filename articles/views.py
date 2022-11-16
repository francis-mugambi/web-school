from django.shortcuts import render
from .models import article
from django.views.generic import ListView



def how_to_articles_view(request):
    foot = article.objects.all().order_by('-id')[:3]
    articles = article.objects.order_by('-id')[::2]
    articles2 = article.objects.order_by('-id')[1::2]
    context={
        'iteams':foot,
        'object_list':articles,
        'object_list2':articles2
    }
    return render(request, 'articles/how_to_articles.html',context)

def article_view(request, str):
    foot = article.objects.all().order_by('-id')[:3]
    articles = article.objects.get(url_name=str)
    context={
        'iteams':foot,
        'article':articles
    }
    return render(request, 'articles/article.html',context)

