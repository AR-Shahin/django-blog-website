
from typing import Any
from django.core.cache import cache
from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from django.views.generic import TemplateView,DetailView,ListView,CreateView
from .models import *
from .form import *
from .seeder import *

class CommonView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().order_by("-id")
        return context
    pass
    

class HomeView(CommonView,TemplateView):
   
    cache.clear()
    # run_seeder(delete=True)
    # create_slider()
    # create_category()
    # create_sub_category()
    # create_tag()
    # run_seeder(delete=True)
    # create_posts()
  
    
    template_name = "frontend/pages/home.html"
    
    def get_context_data(self, **kwargs: Any):
        
        context = super().get_context_data(**kwargs)
        
        # context["categories"] = Category.objects.all().order_by("-id")
        
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
        
        context["ars"] = "Shahin"
        
        
            
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
    
    
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            
            return self.handle_page_out_of_range(request)
        
    def handle_page_out_of_range(self, request):

        return render(request, 'frontend/errors/out_of_range.html', status=404) 

class AboutView(CommonView,TemplateView):
        
    template_name = "frontend/pages/about.html"


class ContactView(CreateView):
    model = Contact
    form_class = ContactUsForm
    template_name = "frontend/pages/contact.html"
    success_url = '/contact'
    
    def form_valid(self, form):
        # I can add here custom logic
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        
        # Add your logic here to do something with the form data
        print(f"Name: {name}, Email: {email}, Message: {message}")

        return super().form_valid(form)
    
class CategoryView(TemplateView):
    
    template_name = "frontend/pages/category.html"
    

    
class SearchView(TemplateView):
    
    template_name = "frontend/pages/search.html"



class BlogView(ListView):
    
    model = Post
    template_name = "frontend/pages/blog.html"
    context_object_name = 'posts'  
    paginate_by = 15
    
    
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            
            return self.handle_page_out_of_range(request)

    def handle_page_out_of_range(self, request):

        return render(request, 'frontend/errors/out_of_range.html', status=404)
    
    def get_queryset(self):
       
        return self.model.objects.order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['popular_posts'] = self.model.objects.select_related("category").filter(view__gte=5).all()[:5]
        context['trending_posts'] = self.model.objects.select_related("category").filter(trending=True).all()[:5]
        context['latest_posts'] = self.model.objects.select_related("category").order_by("-created_at").all()[:5]
        context["categories"] = Category.objects.all()
        context["tags"] = Tag.objects.all()

        return context