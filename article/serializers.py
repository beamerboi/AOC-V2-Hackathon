from rest_framework import serializers
from .models import Article, ArticleType



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleSecondarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', )


class ArticleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleType
        fields = '__all__'