
from django.contrib import admin
from django.urls import path
from .views import *


app_name = "frontend"


urlpatterns = [
    path("", HomeView.as_view(),name="home"),
    path("about", AboutView.as_view(),name="about"),
    path("contact", ContactView.as_view(),name="contact"),
    path("category", CategoryView.as_view(),name="category"),
    path("single/<slug:slug>", SingleView.as_view(),name="single"),
    path("search", SearchView.as_view(),name="search"),
]
