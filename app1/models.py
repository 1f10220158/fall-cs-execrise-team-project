from django.db import models
from django.utils import timezone

class User(models.Model):
    user_id = models.CharField(
        max_length = 200,
        primary_key = True,
        default = '匿名ID',
    )
    password = models.CharField(
        max_length = 200,
    )
    
    def __str__(self):
        return self.user_id

class Article(models.Model):
    article_id = models.AutoField(
        primary_key = True,
    )
    user_id = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        default = "default_user_id",
    )
    article_data = models.FileField(
        upload_to = '',
        default = "default_file_path"
    )
    post_time = models.DateTimeField(
        default = timezone.now,
    )
    title = models.CharField(
        max_length = 200,
    )
    content = models.TextField(
        blank = True,
        null = True,
    )
    answer = models.TextField(
        default = "default_answer",
    )

    #ログイン中のIDを使う投稿は"1",匿名は"0"
    login_or_anonymous = models.IntegerField(
        default = 0,
    )

    def __str__(self):
        return self.article_id

class TimeforOfficial(models.Model):
    user_id = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        primary_key = True,
        default ='default',
    )
    clear_time = models.DateTimeField(
        default = timezone.now,
    )

    def __str__(self):
        return self.user_id

