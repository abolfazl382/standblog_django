from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ArticleManager(models.Manager):
    def counter(self):
        return self.all().count()

    def published(self):
        return self.filter(published=True)

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    objects = ArticleManager()

    def __str__(self):
        return f"{self.title} - {self.body[:30]} ..."
