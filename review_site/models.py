from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
    game_name = models.ForeignKey()

class Reviews(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='game_review')
    title = models.CharField(max_length=200, blank=False, null=False)
    game = models.ForeignKey(Game,)
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rate the game from 1 to 5"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    date_played = models.DateTimeField()
    game_duration = models.PositiveIntegerField(help_text="Game time in minutes")
    player_count = models.PositiveIntegerField

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.review}"