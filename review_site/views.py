from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from review_site.models import Game, Review
from .forms import ReviewForm

# Create your views here.

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
    
class Reviews(ListView):
    model = Review
    template_name = 'reviews.html' 
    context_object_name = 'reviews'         

class ReviewDetail(DetailView):
    model = Review
    template_name = 'reviewsinfo.html'
    context_object_name = 'review'

class AddReview(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'add_review.html'
    # success_url = reverse_lazy('#')

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

