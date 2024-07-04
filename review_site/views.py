from django.shortcuts import render
from django.views.generic import ListView, DetailView
from review_site.models import Game

# Create your views here.
# def base_view(request):
#     return render(request, 'base.html')

# def index_view(request):
#     return render(request, 'base.html')

# def reviews_page_view(request):
#     return render(request, 'base.html')

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

# def profile_view(request):
#     return render(request, 'base.html')

# def post_review_view(request):
#     return render(request, 'base.html')

# def register_view(request):
#     return render(request, 'base.html')

# def login_view(request):
#     return render(request, 'base.html')