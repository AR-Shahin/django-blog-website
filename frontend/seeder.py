from django.db.models import Min,Max

from .models import *
from helpers.helper import *
from .fake_data import *

TAGS = ["Business", "Culture", "Sport", "Food", "Politics" ,"Celebrity" ,"Startups","Travel"]

SLIDERS = [
    {
        "order" : 1,
        "title" : "17 Pictures of Medium Length Hair in Layers That Will Inspire Your New Haircut",
        "content" : "The Best Homemade Masks for Face (keep the Pimples Away)The Best Homemade Masks for Face (keep the Pimples Away)",
        "image" : "images/sliders/post-slide-1.jpg"
    },
     {
        "order" : 2,
        "title" : "13 Amazing Poems from Shel Silverstein with Valuable Life Lessons",
        "content" : "The Best Homemade Masks for Face (keep the Pimples Away)The Best Homemade Masks for Face (keep the Pimples Away)",
        "image" : "images/sliders/post-slide-2.jpg"
    },
    {
        "order" : 3,
        "title" : "The Best Homemade Masks for Face (keep the Pimples Away)",
        "content" : "The Best Homemade Masks for Face (keep the Pimples Away)The Best Homemade Masks for Face (keep the Pimples Away)",
        "image" : "images/sliders/post-slide-3.jpg"
    },
    
]

def create_slider():
    for slider in SLIDERS:
        Slider.objects.create(
            title = slider["title"],
            content = slider["content"],
            order = slider["order"],
            image = slider["image"],
        )
        

def create_category():
    categories = ["Sports","Culture","Politics","Science","Technology","Government"]
    
    for category in categories:
        Category.objects.create(
            title = category,
            image="images/category/post-landscape-1.jpg"
        )
    
def create_sub_category():
    categories = ["Sports 1","Politics 2","Science 1","Technology 1","Culture","Sports","Culture","Politics","Science","Technology" ]
    
    model = Category
    
    for category in categories:
        SubCategory.objects.create(
            title = category,
            category = Category.objects.get(pk=rand_int(get_min_pk(model),get_max_pk(model)))
        )
        
def create_tag():
    for tag in TAGS:
        Tag.objects.create(name=tag)
        

def create_posts():
    
    for i in range(0,60):
        for post in POSTS:
            p = Post.objects.create(
                category = Category.objects.get(pk=rand_int(get_min_pk(Category),get_max_pk(Category))),
                sub_category = SubCategory.objects.get(pk=rand_int(get_min_pk(SubCategory),get_max_pk(SubCategory))),
                title = post["title"] + "-" + str(rand_int(1,1000))  + "-" + str(rand_int(1,1000)),
                description = post["description"],
                image = POST_IMAGES[rand_int(0,(len(POST_IMAGES) - 1))],
                trending = post["trending"],
                view = rand_int(1,20),
            )
            p.tags.set([
            Tag.objects.get(pk=rand_int(get_min_pk(Tag),get_max_pk(Tag))),
            Tag.objects.get(pk=rand_int(get_min_pk(Tag),get_max_pk(Tag))),
            Tag.objects.get(pk=rand_int(get_min_pk(Tag),get_max_pk(Tag))),
            ])


        
        
def delete_all_data():
    
    Slider.objects.all().delete()
    Category.objects.all().delete()
    SubCategory.objects.all().delete()
    Tag.objects.all().delete()
    Post.objects.all().delete()
    

def run_seeder(delete=False):
    if delete:
        delete_all_data()

    # create_slider()
    # create_category()
    # create_sub_category()
    # create_tag()
    # create_posts()
