from django import forms

CHART__CHOICES = (
   ('#1', 'Bar chart'),
   ('#2', 'Pie chart'),
   ('#3', 'Line chart')
   )

class RecipeSearchForm(forms.Form): 
   recipe_name = forms.CharField(max_length=120, required=False)
   ingredients = forms.CharField(max_length=1000, required=False)
   chart_type = forms.ChoiceField(choices=CHART__CHOICES)
