from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView
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

    # def get_object(self):
    #     game_id = self.kwargs.get('pk')
    #     review_id = self.kwargs.get('review_id')
    #     try:
    #         return Review.objects.get(pk=review_id, game_id=game_id)
    #     except Review.DoesNotExist:
    #         raise Http404("No review found matching the query")

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
