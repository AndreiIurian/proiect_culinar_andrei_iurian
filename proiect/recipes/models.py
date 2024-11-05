from django.db import models


class Recipe(models.Model):

     recipe_name = models.CharField(max_length=100)
     execution_time = models.CharField(max_length=20)
     vegetarian = models.BooleanField(default=False)
     vegan = models.BooleanField(default=False)
     glutenfree = models.BooleanField(default=False)
     lactosefree = models.BooleanField(default=False)
     created_at = models.DateTimeField(auto_now_add=True, blank=True)
     instructions = models.TextField(blank=True)
     ingredients = models.TextField(blank=True)

     def __str__(self):
         return f"{self.recipe_name} - {self.execution_time}"

