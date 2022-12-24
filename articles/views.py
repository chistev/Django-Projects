from django.http import HttpResponse
from django.shortcuts import render
from .models import Article


def home(request):
    articles = Article.objects.all().order_by('date')  # order by a defined field in the models
    return render(request, 'articles/index.html', {'articles': articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})



