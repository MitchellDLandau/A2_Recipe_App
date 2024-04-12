from django import forms
from .models import Recipe

CHART__CHOICES = (
   ('#1', 'Bar chart'),
   ('#2', 'Pie chart'),
   ('#3', 'Line chart')
   )

DIFFICULTY_CHOICES = (
    ("", " "),
    ("Easy", "Easy"),
    ("Medium", "Medium"),
    ("Hard", "Hard"),
)

class RecipeSearchForm(forms.Form): 
   recipe_name = forms.CharField(max_length=120, required=False)
   ingredients = forms.CharField(max_length=1000, required=False)
   chart_type = forms.ChoiceField(choices=CHART__CHOICES)


class RecipeAddForm(forms.ModelForm):
   class Meta:
      model = Recipe
      fields = ["name", "cooking_time", "difficulty", "ingredients", "pic"]