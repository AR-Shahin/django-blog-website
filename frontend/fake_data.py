from helpers.helper import *
from .models import *

POST_IMAGES = [
    "images/posts/post-sq-1.jpg","images/sliders/post-slide-2.jpg",
    "images/posts/post-sq-4.jpg", "images/posts/post-portrait-5.jpg",
    "images/posts/post-sq-3.jpg","images/posts/post-portrait-6.jpg",
    "images/posts/post-sq-5.jpg","images/posts/post-portrait-7.jpg",
    "images/posts/post-sq-6.jpg","images/posts/post-portrait-8.jpg",
    "images/posts/post-landscape-1.jpg","images/posts/post-landscape-2.jpg",
    "images/posts/post-landscape-3.jpg","images/posts/post-landscape-4.jpg",

]

POSTS = [
    {
        "title" : "What is the son of Football " + str(rand_int(1,500)) +" Coach John Gruden, Deuce Gruden ars Now?!",
        "description" : "Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio placeat exercitationem magni voluptates dolore. Tenetur fugiat voluptates quas.",
        "trending" : True,
        # "category" : Category.objects.get(pk=rand_int(get_min_pk(Category),get_max_pk(Category))),
        # "sub_category" : SubCategory.objects.get(pk=rand_int(get_min_pk(SubCategory),get_max_pk(SubCategory))),
        # "tags" : [
        #     Tag.objects.get(pk=rand_int(get_min_pk(Tag),get_max_pk(Tag))),
        #     Tag.objects.get(pk=rand_int(get_min_pk(Tag),get_max_pk(Tag))),
        #     Tag.objects.get(pk=rand_int(get_min_pk(Tag),get_max_pk(Tag))),
        # ]
    }
]

