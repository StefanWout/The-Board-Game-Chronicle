from django.contrib import admin
from django.urls import path, include
from review_site.views import Games, GameDetail, AddReview, Reviews, ReviewDetail, Index, ProfileView, EditReview, DeleteReview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('games/', Games.as_view(), name='games'),
    path('games/<int:pk>/', GameDetail.as_view(), name='game_detail'),
    path('reviews/', Reviews.as_view(), name='reviews'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review'),
    path('add_review/', AddReview.as_view(), name='add_review'),
    path('edit_review/<int:pk>', EditReview.as_view(), name='edit_review'),
    path('delete_review/<int:pk>', DeleteReview.as_view(), name='delete_review'),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
    path("profile/<int:pk>", ProfileView.as_view(), name='profile'),
    path('accounts/', include('allauth.urls')),
]
