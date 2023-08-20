from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *



class HomeView(TemplateView):
        
    template_name = "frontend/pages/home.html"
    
    def get_context_data(self, **kwargs: Any):
        
        context = super().get_context_data(**kwargs)

        context["sliders"] = Slider.objects.all().order_by("order")
            
        return context
    
    
class AboutView(TemplateView):
        
    template_name = "frontend/pages/about.html"


class ContactView(TemplateView):
        
    template_name = "frontend/pages/contact.html"
    
    
class CategoryView(TemplateView):
    
    template_name = "frontend/pages/category.html"
    
class SingleView(TemplateView):
    
    template_name = "frontend/pages/single.html"
    
class SearchView(TemplateView):
    
    template_name = "frontend/pages/search.html"
