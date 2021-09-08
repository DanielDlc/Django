from django.urls import path, include
from .views import *

urlpatterns = [
    path('home', index, name='home'),
    path('contact', contact, name='contact'),
    path('about', about, name='about')

]
