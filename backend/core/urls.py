from django.urls import path

from core.views import *

urlpatterns = [
    path("search/", search_food_trucks, name="search_food_trucks"),
]
