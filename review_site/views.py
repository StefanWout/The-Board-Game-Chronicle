from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from django.views.generic.edit import DeleteView
from review_site.models import Game, Review, Comment, User
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ReviewForm

# Create your views here.

class Index(ListView):
    model = Game
    template_name = 'index.html'
    context_object_name = 'games' 

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
    
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

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
    form_class = ReviewForm
    template_name = 'edit_review.html'
    context_object_name = 'review'

    def get_success_url(self):
        return reverse('review', args=[self.object.id])

    def form_valid(self, form):
        if form.instance.user != self.request.user:
            messages.add_message(self.request, messages.ERROR, 'You are not authorized to edit this review!')
            return redirect('review', pk=self.object.pk)
        review = form.save(commit=False)
        review.approved = False
        review.save()
        messages.add_message(self.request, messages.SUCCESS, 'Review Updated!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Error updating review!')
        return super().form_invalid(form)

class DeleteReview(DeleteView):
    model = Review
    template_name = 'confirm_delete.html'
    context_object_name = 'review'
    
    def get_success_url(self):
        user_pk = self.request.user.pk  # Get the current user's pk
        messages.success(self.request, 'Review deleted!')
        return reverse('profile', kwargs={'pk': user_pk})
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            return super().delete(request, *args, **kwargs)
        else:
            messages.error(request, 'You can only delete your own reviews!')
            return HttpResponseRedirect(reverse_lazy('profile'))