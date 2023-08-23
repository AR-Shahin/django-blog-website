from helpers.helper import *
from .models import *


POSTS = [
    {
        "title" : "What is the son of Football Coach John Gruden, Deuce Gruden ars Now?!",
        "description" : "Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio placeat exercitationem magni voluptates dolore. Tenetur fugiat voluptates quas.",
        "trending" : True,
        "category" : Category.objects.get(pk=rand_int(get_min_pk(Category),get_max_pk(Category))),
        "sub_category" : SubCategory.objects.get(pk=rand_int(get_min_pk(SubCategory),get_max_pk(SubCategory))),
        "image" : "images/sliders/post-slide-2.jpg",
        "tags" : [
            Tag.objects.get(pk=rand_int(get_min_pk(Tag),get_max_pk(Tag))),
            Tag.objects.get(pk=rand_int(get_min_pk(Tag),get_max_pk(Tag))),
            Tag.objects.get(pk=rand_int(get_min_pk(Tag),get_max_pk(Tag))),
        ]
    }
]

