from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Game, Reviews, Comment

# Register your models here.
class ReviewsAdmin(SummernoteModelAdmin):

    list_display = ('game', 'title', 'status', 'created_at')
    search_fields = ['user', 'game', 'created_at']
    list_filter = ('status', 'created_at',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('review_text',)

# Register your models here.
admin.site.register(Comment)
admin.site.register(Reviews)
admin.site.register(Game)