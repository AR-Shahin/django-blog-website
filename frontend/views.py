from django.shortcuts import render
from django.views.generic import TemplateView




class HomeView(TemplateView):
        
    template_name = "frontend/pages/home.html"
    
    
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
