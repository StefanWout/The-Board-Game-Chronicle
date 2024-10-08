from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Game, Review, Comment

class ReviewsAdmin(SummernoteModelAdmin):

    list_display = ('game', 'title', 'status', 'created_at')
    search_fields = ['user', 'game', 'created_at']
    list_filter = ('status', 'created_at',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('review_text',)

# Register your models here.
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(Game)