from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

# Create your views here.

def main(request):
    return render(request, 'recipes/main.html')

class RecipeListView(ListView):
   model = Recipe
   template_name = 'recipes/home.html'

class RecipeDetailView(DetailView):
   model = Recipe
   template_name = 'recipes/detail.html'
   context_object_name = 'recipe'