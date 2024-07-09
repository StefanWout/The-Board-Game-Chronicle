"""
URL configuration for board_game_chronicle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from review_site.views import Games, GameDetail, AddReview, Reviews, ReviewDetail, Index, ProfileView,EditReview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('games/', Games.as_view(), name='games'),
    path('games/<int:pk>/', GameDetail.as_view(), name='game_detail'),
    path('reviews/', Reviews.as_view(), name='reviews'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review'),
    path('add_review/', AddReview.as_view(), name='add_review'),
    path('edit_review/<int:pk>', EditReview.as_view(), name='edit_review'),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
    path("profile/<int:pk>", ProfileView.as_view(), name = 'profile'),
]
