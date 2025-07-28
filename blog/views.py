from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from blog.models import Article, Category


def articles(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'blog/post-details.html', {'article': article, 'page':'details'})

def article_list(request):
    arts = Article.objects.published().order_by('-created')
    page = request.GET.get('page')

    paginator = Paginator(arts, 1)
    objects_list = paginator.get_page(page)

    for art in objects_list:
        art.body = art.body[:50]

    return render(request, 'blog/post-list.html', context={'articles': objects_list ,'page':'articles'})

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    # arts = category.article_set.published().order_by('-created')
    arts = category.articles.published().order_by('-created')
    return render(request, 'blog/post-list.html', context={'articles': arts, 'page':'articles'})


