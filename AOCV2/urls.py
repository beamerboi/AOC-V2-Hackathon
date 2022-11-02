from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('account/', include('accounts.urls')),
    path('article/', include('article.urls')),
    path('contact/', include('contact.urls')),
]
