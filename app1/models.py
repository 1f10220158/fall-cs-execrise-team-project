from django.db import models
from django.utils import timezone

class User(models.Model):
    user_id = models.CharField(max_length=200, primary_key=True, default='default')
    password = models.CharField(max_length=200, default='')
    time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user_id

class Article(models.Model):
    article_id = models.CharField(max_length=200, primary_key=True, default='default')
    user_id = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        default='default'
        )
    article_url = models.URLField(max_length=200, default='default')
    time = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200, default='default')
    content = models.TextField(null=True)

    def __str__(self):
        return self.article_id

class TimeforOfficial(models.Model):
    user_id = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        primary_key = True,
        default='default'
        )
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_id

