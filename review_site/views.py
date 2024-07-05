from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
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
        
class GameDetail(DetailView)  :
    model = Game
    template_name = 'gameinfo.html'
    context_object_game = 'game'     

class ReviewsPage(ListView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews.html'
    success_url = reverse_lazy('games/<int:pk>')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assuming the Review model has a user field
        return super().form_valid(form)

# def profile_view(request):
#     return render(request, 'base.html')

# def post_review_view(request):
#     return render(request, 'base.html')

# def register_view(request):
#     return render(request, 'base.html')

# def login_view(request):
#     return render(request, 'base.html')