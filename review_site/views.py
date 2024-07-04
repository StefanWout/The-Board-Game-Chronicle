from django.shortcuts import render
from .games_data_load import main

# Create your views here.
def base_view(request):
    return render(request, 'base.html')

def index_view(request):
    return render(request, 'base.html')

def reviews_page_view(request):
    return render(request, 'base.html')

def games_view(request):
    games_data = main()
    return render(request, 'games.html', {'games_data': games_data})

def profile_view(request):
    return render(request, 'base.html')

def post_review_view(request):
    return render(request, 'base.html')

def register_view(request):
    return render(request, 'base.html')

def login_view(request):
    return render(request, 'base.html')