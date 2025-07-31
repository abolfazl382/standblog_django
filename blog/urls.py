from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('articles', views.article_list, name='articles'),
    path('articles/<slug:slug>', views.article_details, name='article'),
    path('category/<int:id>', views.category_detail, name='category_detail'),
    path('search', views.search, name='search'),

]