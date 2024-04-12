from django.urls import path
from .views import RecipeListView, RecipeDetailView, ContactView,add_recipe, main
from . import views

app_name = 'recipes'  

urlpatterns = [
   path("", main, name="main_view"),
   path("list/", RecipeListView.as_view(), name="list"), 
   path("list/<pk>", RecipeDetailView.as_view(), name="detail"),
   path("add/", add_recipe, name="add"),
   path("contact/", ContactView.as_view(), name="contact")
]