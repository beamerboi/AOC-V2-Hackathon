from django.contrib import admin
from .models import ArticleType, Article, Donation


admin.site.register(ArticleType)
admin.site.register(Article)
admin.site.register(Donation)

# Register your models here.
