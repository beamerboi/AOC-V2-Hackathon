from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.ArticleCreateAPIView.as_view()),
    path('/', views.ArticleListAPIView.as_view()),
    path('<int:pk>/', views.ArticleDetailAPIView.as_view()),
    path('me/', views.ArticleUserListAPIView.as_view()),
    path('article-type/', views.ArticleTypeListAPIView.as_view()),
]