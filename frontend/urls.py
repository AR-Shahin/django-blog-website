
from django.contrib import admin
from django.urls import path
from .views import *


app_name = "frontend"


urlpatterns = [
    path("", HomeView.as_view(),name="home"),
    path("about", AboutView.as_view(),name="about"),
    path("blogs", BlogView.as_view(),name="blog"),
    path("contact", ContactView.as_view(),name="contact"),
    path("category/<slug:category_slug>", CategoryWisePostView.as_view(),name="category"),
    path("single/<slug:slug>", SingleView.as_view(),name="single"),
    path("search", SearchView.as_view(),name="search"),
]
