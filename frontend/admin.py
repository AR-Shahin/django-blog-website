from django.contrib import admin

from .models import *

admin.site.register([Slider,Category,SubCategory,Tag,Post,Contact])