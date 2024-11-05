from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from recipes.forms import RecipesForm
from recipes.forms import RecipeInstructionsForm
from recipes.models import Recipe
from django.contrib import messages

class CreateRecipeView(CreateView):
    model = Recipe
    template_name = 'forms.html'
    #fields = ['recipe_name', 'execution_time', 'vegetarian', 'vegan', 'glutenfree', 'lactosefree']
    form_class = RecipesForm

    def get_form_kwargs(self):
        data = super(CreateRecipeView, self).get_form_kwargs()
        data.update({'pk': None})
        return data

    def get_success_url(self):
        messages.success(self.request, 'Recipe created successfully.')
        return reverse('recipes:lista_retete')

class RecipeView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_index.html'

class UpdateRecipeView(UpdateView):
    model = Recipe
    #fields = ['recipe_name', 'execution_time', 'vegetarian', 'vegan', 'glutenfree', 'lactosefree']
    template_name = 'forms.html'
    form_class = RecipesForm

    def get_form_kwargs(self):
        data = super(UpdateRecipeView, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
        return data

    def get_success_url(self):
        messages.success(self.request, 'Recipe updated successfully.')
        return reverse('recipes:lista_retete')

class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = 'forms.html'
    context_object_name = 'recipe'

    def get_success_url(self):
        messages.success(self.request, 'Recipe deleted successfully.')
        return reverse('recipes:lista_retete')

class RecipeDetailView(UpdateView):
    model = Recipe
    form_class = RecipeInstructionsForm
    template_name = 'recipes/recipe_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Recipe, pk=self.kwargs['pk'])

    def form_valid(self, form):
        messages.success(self.request, 'Recipe instructions and ingredients updated successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('recipes:lista_retete')