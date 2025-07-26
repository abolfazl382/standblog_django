from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('articles', views.article_list, name='articles'),
    path('articles/<slug:slug>', views.articles, name='article'),
    path('category/<int:id>', views.category_detail, name='category_detail'),

]