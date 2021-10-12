from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views


route = DefaultRouter()
route.register('tags', views.TagViewSet)
route.register('ingredient', views.IngredientViewSet)
route.register('recipes', views.RecipeViewSet)


app_name = 'recipe'

urlpatterns = [
    path('', include(route.urls))
]
