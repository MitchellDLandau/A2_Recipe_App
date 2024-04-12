from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse
import pandas as pd
from .utils import get_recipe_from_id, get_chart
from .models import Recipe
from .forms import RecipeSearchForm, RecipeAddForm
import json

def main(request):
    return render(request, 'recipes/main.html')

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/home.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        recipe_name = self.request.GET.get('recipe_name')
        ingredients = self.request.GET.get('ingredients')

        combine_query = Q()

        if recipe_name:
            combine_query &= Q(name__icontains=recipe_name)
        if ingredients:
            for ingredient in ingredients.split(','):
                combine_query |= Q(ingredients__icontains=ingredient.strip())
        queryset = queryset.filter(combine_query).distinct()

        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RecipeSearchForm(self.request.GET)

        if not context["object_list"]:
            error_message = "No recipes match that description."
            messages.error(self.request, error_message)
            context["error_message"] = error_message
            return context

        if "chart_type" in self.request.GET:
            chart_type = self.request.GET["chart_type"]
            queryset = self.get_queryset()
            data = pd.DataFrame(queryset.values())
            ingredients = data['ingredients']
            name = data['name']
            chart_data = {
                "name": name,
                "ingredients": ingredients,
            }

            if chart_type == "#1":
                chart_data["name"] = chart_data.get("name")
            elif chart_type == '#2':
               size = data['ingredients']
               labels = data['name']
            else:
                chart_data["labels"] = None
            chart_image = get_chart(chart_type, chart_data)
            context["chart_image"] = chart_image

        return context
    
class AddRecipeView(LoginRequiredMixin, CreateView):
   model = Recipe
   template_name = 'recipes/add.html'
   fields = ['name', 'cooking_time', 'difficulty', 'ingredients', 'pic']

class ContactView(LoginRequiredMixin, ListView):
    template_name = 'recipes/contact.html'
    model = Recipe
    context_object_name = 'contact'

class RecipeDetailView(LoginRequiredMixin, DetailView):
   model = Recipe
   template_name = 'recipes/detail.html'
   context_object_name = 'recipe'

def add_recipe(request):
   if request.method == 'POST':
      form = RecipeAddForm(data=request.POST, files=request.FILES)
      if form.is_valid():
         form.save()
         return redirect(reverse('recipes:list'))
   else:
      form = RecipeAddForm()

   previous_url = request.META.get('HTTP_REFERER')

   context = {'form': form, 'previous_url': previous_url}
   return render(request, 'recipes/add.html', context)