from django.shortcuts import render

from blog.models import Article


def articles(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'blog/post-details.html', {'article': article, 'page':'details'})

def article_list(request):
    arts = Article.objects.published().order_by('-created')
    for art in arts:
        art.body = art.body[:50]
    return render(request, 'blog/post-list.html', context={'articles': arts, 'page':'articles'})
