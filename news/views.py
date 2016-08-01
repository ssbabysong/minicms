# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
 
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Column,Article
from django.shortcuts import redirect 
 
# def index(request):
#     return HttpResponse(u'学习Django')

 
# def column_detail(request, column_slug):
#     return HttpResponse('column slug: ' + column_slug)
 
 
def article_detail(request, pk,article_slug):
	article = Article.objects.get(pk=pk)
	if article_slug != article.slug:
		return redirect(article, permanent=True)
	return render(request, 'news/article.html', {'article': article})

def index(request):
	home_display_columns = Column.objects.filter(home_display=True)
	nav_display_columns = Column.objects.filter(nav_display=True)
	return render(request, 'index.html', {'home_display_columns': home_display_columns,'nav_display_columns': nav_display_columns,})
	
def column_detail(request, column_slug):
	column = Column.objects.get(slug=column_slug)
	return render(request, 'news/column.html', {'column': column})
# def article_detail(request, article_slug):
#     article = Article.objects.filter(slug=article_slug)[0]
#     return render(request, 'news/article.html', {'article': article})