from django.db import models
from AOCV2 import settings


class ArticleType(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=30)
    delay = models.DateField()
    article_type = models.ForeignKey(ArticleType, on_delete=models.CASCADE)
    picture = models.ImageField(default="images/default.png", upload_to="images/")
    beneficiary = models.CharField(max_length=30)
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    description = models.TextField(null=True)
    amount = models.IntegerField(default=1)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

