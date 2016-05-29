# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
 
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Column
 
 
# def index(request):
#     return HttpResponse(u'学习Django')

 
# def column_detail(request, column_slug):
#     return HttpResponse('column slug: ' + column_slug)
 
 
# def article_detail(request, article_slug):
#     return HttpResponse('article slug: ' + article_slug)
def index(request):
    columns=Column.objects.all()
    return render(request, 'index.html', {'columns': columns})

def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column': column})
 
 
# def article_detail(request, article_slug):
#     article = Article.objects.get(slug=article_slug)
#     return render(request, 'news/article.html', {'article': article})
def article_detail(request, article_slug):
    article = Article.objects.filter(slug=article_slug)[0]
    return render(request, 'news/article.html', {'article': article})