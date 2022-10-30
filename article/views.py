from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView
from .models import Article, ArticleType
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ArticleSerializer, ArticleTypeSerializer


class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
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