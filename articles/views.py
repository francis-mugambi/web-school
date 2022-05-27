from django.shortcuts import render
from .models import article
from django.views.generic import ListView

class how_to_articles_view(ListView):
    model = article
    queryset = article.objects.order_by('-id')[:4]
    template_name = 'articles/how_to_articles.html'

def article_view(request, str):
    foot = article.objects.all().order_by('-id')[:3]
    articles = article.objects.get(url_name=str)
    context={
        'iteams':foot,
        'article':articles
    }
    return render(request, 'articles/article.html',context)

