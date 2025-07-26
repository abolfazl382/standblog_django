from django.shortcuts import render, get_object_or_404

from blog.models import Article, Category


def articles(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'blog/post-details.html', {'article': article, 'page':'details'})

def article_list(request):
    arts = Article.objects.published().order_by('-created')
    for art in arts:
        art.body = art.body[:50]
    return render(request, 'blog/post-list.html', context={'articles': arts, 'page':'articles'})

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    # arts = category.article_set.published().order_by('-created')
    arts = category.articles.published().order_by('-created')
    for art in arts:
        art.body = art.body[:50]
    return render(request, 'blog/post-list.html', context={'articles': arts, 'page':'articles'})


