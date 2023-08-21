from typing import Any
import random
from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from .models import *



class HomeView(TemplateView):
        
    template_name = "frontend/pages/home.html"
    
    def get_context_data(self, **kwargs: Any):
        
        context = super().get_context_data(**kwargs)
        
        context["categories"] = Category.objects.all()
        
        context["second_section"] = context["categories"][1]
        third_section = context["categories"][2]
        # fourth_section = context["categories"][3]
        
        all_posts = Post.objects.select_related("category").order_by("-created_at")
        context["second_section_posts"] = all_posts.filter(category=context["second_section"].id).all()
     
        context["sliders"] = Slider.objects.filter(status=True).all().order_by("order")
        context["latest_posts"] = Post.objects.select_related("category").order_by("-created_at")[:3]
        context["latest_posts_more"] = Post.objects.order_by("-created_at")[3:6]
        context["trending_posts"] = Post.objects.filter(trending=True).order_by("-created_at")[:5]
        
        context["first_post"] = context["latest_posts"][random.randint(0, 2)]
        
            
        return context
    
class SingleView(DetailView):
    
    model = Post
    context_object_name = 'post' 
    slug_field = 'slug'
    
    template_name = "frontend/pages/single.html" 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        context["categories"] = Category.objects.all()
        context["tags"] = Category.objects.all()

        return context
    

class AboutView(TemplateView):
        
    template_name = "frontend/pages/about.html"


class ContactView(TemplateView):
        
    template_name = "frontend/pages/contact.html"
    
    
class CategoryView(TemplateView):
    
    template_name = "frontend/pages/category.html"
    

    
class SearchView(TemplateView):
    
    template_name = "frontend/pages/search.html"
