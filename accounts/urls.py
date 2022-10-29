from django.urls import path
from . import views

urlpatterns = [
    path('account-type/', views.AccountTypeSerializerAPIListView.as_view()),
    path('logout/', views.BlacklistRefreshView.as_view(), name="logout"),
    path('me/update/', views.ProfileUpdateAPIView.as_view()),
    path('me/', views.ProfileDetailAPIView.as_view()),

]