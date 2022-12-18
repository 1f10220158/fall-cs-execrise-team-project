from django.db import models
from django.utils import timezone

class User(models.Model):
    user_id = models.CharField(
        max_length = 200,
        primary_key = True,
        default = '匿名ID',
    )
    password = models.CharField(max_length=200, default='')
    time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user_id

class Article(models.Model):
    article_id = models.CharField(
        primary_key = True,
        editable = False,
        max_length = 32,
        default = ""
    )
    user_id = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        null = True,
        blank = True,
    )
    article_data = models.FileField(upload_to='', null=True)
    time = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200, default='default')
    content = models.TextField(null=True, unique=False)

    def __str__(self):
        return self.article_id

class TimeforOfficial(models.Model):
    user_id = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        primary_key = True,
        default ='default',
    )
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_id

