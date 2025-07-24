from blog.models import Article

def recent_articles(request):
    recent_arts = Article.objects.order_by('-created')

    return {'recent_articles': recent_arts}