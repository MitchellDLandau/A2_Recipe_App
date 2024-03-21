from django.test import TestCase

# Create your tests here.

from .models import Recipe

class RecipeModelTest(TestCase):

    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Recipe.objects.create(name='Pizza',
                              cooking_time=30,
                              difficulty='easy',
                              ingredients='flour, tomato, cheese')
        
    def test_name_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_cooking_time_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('cooking_time').verbose_name
        self.assertEquals(field_label, 'cooking time')

    def test_difficulty_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('difficulty').verbose_name
        self.assertEquals(field_label, 'difficulty')

    def test_difficulty_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('difficulty').max_length
        self.assertEquals(max_length, 20)

    def test_ingredients_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('ingredients').verbose_name
        self.assertEquals(field_label, 'ingredients')

    def test_ingredients_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('ingredients').max_length
        self.assertEquals(max_length, 1000)

    def test_object_name_is_name(self):
        recipe = Recipe.objects.get(id=1)
        expected_object_name = f'{recipe.name}'
        self.assertEquals(expected_object_name, str(recipe))