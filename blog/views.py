from django.shortcuts import render

from blog.models import Article


def articles(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'blog/post-details.html', {'article': article})
