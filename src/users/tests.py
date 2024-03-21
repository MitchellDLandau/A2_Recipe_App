from django.test import TestCase

# Create your tests here.

from .models import User

class UserModelTest(TestCase):

    def setUpTestData():
        # Set up non-modified objects used by all test methods
        User.objects.create(name='Big')

    def test_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)