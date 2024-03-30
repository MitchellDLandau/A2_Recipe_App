from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

# Create your views here.

def main(request):
    return render(request, 'recipes/main.html')

class RecipeListView(LoginRequiredMixin, ListView):
   model = Recipe
   template_name = 'recipes/home.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
   model = Recipe
   template_name = 'recipes/detail.html'
   context_object_name = 'recipe'