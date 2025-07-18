from django.shortcuts import render

from blog.models import Article


def articles(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'blog/post-details.html', {'article': article})
