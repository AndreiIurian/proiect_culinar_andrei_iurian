from django import forms
from django.forms import TextInput, CheckboxInput

from recipes.models import Recipe


class RecipesForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['recipe_name', 'execution_time', 'vegetarian', 'vegan', 'glutenfree', 'lactosefree']

        widgets = {
            'recipe_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Recipe Name'}),
            'execution_time': TextInput(attrs={'class': 'form-control', 'placeholder': 'Execution Time'}),
            'vegetarian': CheckboxInput(attrs={'class': 'form-check-input'}),
            'vegan': CheckboxInput(attrs={'class': 'form-check-input'}),
            'glutenfree': CheckboxInput(attrs={'class': 'form-check-input'}),
            'lactosefree': CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, pk, *args, **kwargs):
        super(RecipesForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        recipe_name_value = self.cleaned_data.get('recipe_name')
        if self.pk:
            if Recipe.objects.filter(recipe_name=recipe_name_value).exclude(id=self.pk).exists():
                self._errors['recipe_name'] = self.error_class(['Reteta deja exista'])
        else:
            if Recipe.objects.filter(recipe_name=recipe_name_value).exists():
                self._errors['recipe_name'] = self.error_class(['Reteta deja exista'])
        return self.cleaned_data

class RecipeInstructionsForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['instructions', 'ingredients']
        widgets = {
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Instructions', 'rows': 10}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingredients', 'rows': 10}),
        }