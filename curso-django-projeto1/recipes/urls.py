from django.urls import path

from recipes.views import contato, home, sobre

urlpatterns = [
    path('', home), # home
    path('contato/', contato), # /sobre/
    path('sobre/', sobre), # /contato/
]
