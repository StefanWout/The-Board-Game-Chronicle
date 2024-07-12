from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Game(models.Model):
    game_name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(null=True)
    min_players = models.IntegerField(null=True)
    max_players = models.IntegerField(null=True)
    playing_time = models.IntegerField(null=True)
    image = models.URLField(null=True)
    def __str__(self):
        return self.game_name

    class Meta:
        verbose_name = 'Game'
        db_table = 'game'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer')
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='review')
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rate the game from 1 to 5"
    )
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    date_played = models.DateField(null=True, help_text="MM/DD/YYY")
    game_duration = models.PositiveIntegerField(null=True, help_text="Game time in minutes")
    player_count = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.user.username}'s review of {self.game.game_name}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.review}"