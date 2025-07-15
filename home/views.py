from django.shortcuts import render

from blog.models import Article


def index(request):
    articles = Article.objects.published()
    return render(request, 'home/index.html', context={'articles': articles})
