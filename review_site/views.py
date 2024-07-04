from django.shortcuts import render

# Create your views here.
def base_view(request):
    return render(request, 'base.html')

def index_view(request):
    return render(request, 'base.html')

def reviews_page_view(request):
    return render(request, 'base.html')

def games_view(request):
    return render(request, 'base.html')

def profile_view(request):
    return render(request, 'base.html')

def post_review_view(request):
    return render(request, 'base.html')

def register_view(request):
    return render(request, 'base.html')

def login_view(request):
    return render(request, 'base.html')