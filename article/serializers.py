from rest_framework import serializers
from .models import Article, ArticleType, Donation
from django.contrib.auth import get_user_model
User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleSecondarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title',)


class ArticleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleType
        fields = '__all__'


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ('seeker', 'amount', 'article', 'visibility')


