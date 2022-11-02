from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView
from .models import Article, ArticleType, Donation
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ArticleSerializer, ArticleTypeSerializer, DonationSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        user = User.objects.get(pk=self.request.user.id)
        type = user.account_type
        serializer.save(author=self.request.user)


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ArticleUserListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        def get_queryset(self):
            return Article.objects.filter(author=self.request.user)


class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ArticleUpdateAPIView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ArticleTypeListAPIView(ListAPIView):
    queryset = ArticleType.objects.all()
    serializer_class = ArticleTypeSerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticatedOrReadOnly, )


class DonationCreateAPIView(CreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        user = User.objects.get(pk=self.request.user.id)
        type = user.account_type
        donor = self.request.user
        amount = serializer.validated_data.get('amount')
        post = serializer.validated_data.get('article')
        post = Article.objects.get(pk=post.id)
        if amount == 0:
            raise ValueError("Cannot be done")
        if post.amount - amount >=0:
            post.amount -= amount
        else:
            raise ValueError('Amount Too much')
        post.save()
        serializer.save(donor=donor)


class DonationListAPIView(ListAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    lookup_field = 'pk'


