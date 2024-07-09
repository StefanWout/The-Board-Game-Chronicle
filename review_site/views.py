from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from review_site.models import Game, Review, Comment, User
from django.contrib.auth.models import User
from .forms import ReviewForm

# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'

class Games(ListView):
    model = Game
    template_name = 'games.html' 
    context_object_name = 'games' 
    
    # DEBUG OPTION

    # def get_queryset(self):
    #     output = Game.objects.all()
    #     print (output[0].id)
        
class GameDetail(DetailView):
    model = Game
    template_name = 'gameinfo.html'
    context_object_name = 'game' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add data from the Review model to the context
        context['reviews'] = Review.objects.filter(game=self.object)
        return context

class Reviews(ListView):
    model = Review
    template_name = 'reviews.html'
    context_object_name = 'reviews'         

class ReviewDetail(DetailView):
    model = Review
    template_name = 'reviewsinfo.html'
    context_object_name = 'review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = self.get_object()
        game = review.game 
        context['game'] = game 
        return context

class AddReview(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'add_review.html'
    success_url = reverse_lazy('reviews')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return self.form_valid(form)
        return render(request, self.template_name, {'form': form})

class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        # Get the User object based on the 'pk' or 'slug' captured in the URL
        pk = self.kwargs.get('pk')
        return get_object_or_404(User, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        # Add data from the Review model to the context
        context['reviews'] = Review.objects.filter(user=user)
        return context

class EditReview(UpdateView):
    model = Review
    template_name = 'edit_review.html'
    form_class = ReviewForm 
    def get_success_url(self):
        # Redirect to the profile page of the user who edited the review
        user_id = self.object.user.pk
        return reverse('profile', kwargs={'pk': user_id})

def delete_recipe(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect(reverse(
        'your_recipes'))