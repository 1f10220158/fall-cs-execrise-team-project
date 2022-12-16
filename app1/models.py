from django.db import models
from django.utils import timezone
class User(models.Model):
    UserID=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    def __str__(self):
        return self.UserID
class Article(models.Model):
    ArticleID=models.CharField(max_length=200)
    userID=models.CharField(max_length=200)
    ArticleData=models.TextField()
class TimeforOfficial:
    UserID=models.CharField(max_length=200)
    time=models.DateTimeField(default=timezone.now)

# Create your models here.
