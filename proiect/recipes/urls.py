from django.urls import path
from recipes import views
from recipes.views import RecipeDetailView

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeView.as_view(), name='lista_retete'),
    path('adaugare/', views.CreateRecipeView.as_view(), name='adaugare'),
    path('<int:pk>/modificare/', views.UpdateRecipeView.as_view(), name='modifica'),
    path('<int:pk>/stergere/', views.DeleteRecipeView.as_view(), name='stergere'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
]