from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Review, Comment
from django.contrib.auth.models import User

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['game', 'title', 'review_text', 'rating', 'date_played', 'game_duration', 'player_count']
        widgets = {'review_text': SummernoteWidget()}

    def __init__(self, *args, **kwargs):
        super(ReviewForm,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

#         def clean(self):
#             cleaned_data = super().clean()
#             password = cleaned_data.get("password")
#             password_confirm = cleaned_data.get("password_confirm")

#             if password and password_confirm and password != password_confirm:
#                 raise forms.ValidationError("Passwords do not match")

#             return cleaned_data