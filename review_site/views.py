from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from review_site.models import Game, Review, Comment
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

# class RegisterView(CreateView):
#     model = UserWarning
#     form_class = RegisterForm
#     template_name = 'register.html'
#     # success_url = reverse_lazy('#')

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.user = request.user
#             review.save()
#             return self.form_valid(form)
#         return render(request, self.template_name, {'form': form})