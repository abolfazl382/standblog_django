from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Article, Category, Comment


def article_details(request, slug):

    article = Article.objects.get(slug=slug)

    if request.method == 'POST' and request.user.is_authenticated:
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        user = request.user
        if body:
            Comment.objects.create(article=article, user=user, body=body, parent_id=parent_id)

    return render(request, 'blog/post-details.html', {'article': article})

def article_list(request):
    arts = Article.objects.published().order_by('-created')
    page = request.GET.get('page')

    paginator = Paginator(arts, 1)
    objects_list = paginator.get_page(page)

    return render(request, 'blog/post-list.html', context={'articles': objects_list})

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    # arts = category.article_set.published().order_by('-created')
    arts = category.articles.published().order_by('-created')
    return render(request, 'blog/post-list.html', context={'articles': arts})

def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page)
    return render(request, 'blog/post-list.html', context={'articles': objects_list})







