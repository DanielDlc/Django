from django.urls import path

from recipes.views import home, recipe
from . import views


urlpatterns = [
    path('', views.home),  # home
    path('recipes/<int:id>/', views.recipe),
]
