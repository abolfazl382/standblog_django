from django.shortcuts import render

from blog.models import Article


def index(request):
    articles = Article.objects.published().order_by('-created')[:5]
    # recent_articles = articles[:3]

    context = {
        'page': 'home',
        'articles': articles,
        # 'recent_articles': recent_articles,
    }

    return render(request, 'home/index.html', context=context)

