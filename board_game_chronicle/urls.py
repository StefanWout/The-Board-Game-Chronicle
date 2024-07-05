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
from django.urls import path
from review_site.views import Games, GameDetail, AddReview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', Games.as_view(), name='games'),
    path('games/<int:pk>/', GameDetail.as_view(), name='game detail'),
    path('add_review/', AddReview.as_view(), name='add reveiw'),
]
   # path('summernote/', include('django_summernote.urls')),
    # path('', views.base_view, name='base'),
    # path('index/', views.index_view, name='index'),
    
    #     path('profile/', views.profile_view, name='profile'),
#     path('post/', views.post_review_view, name='post'),
#     path('register/', views.register_view, name='register'),
#     path('login/', views.login_view, name='login'),