from django.urls import path
from .views import RecipeListView, RecipeDetailView, main

app_name = 'recipes'  

urlpatterns = [
   path("", main, name="main_view"),
   path("list/", RecipeListView.as_view(), name="list"), 
   path("list/<pk>", RecipeDetailView.as_view(), name="detail")
]