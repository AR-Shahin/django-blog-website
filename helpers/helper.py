import random
from django.db.models import Min,Max
from django.db.models import Model

from frontend.models import *

def rand_int(min = 1, max = 10): return random.randint(min, max)
def ars(min = 1, max = 10): return random.randint(min, max)


def get_min_pk(model: Model): return model.objects.aggregate(min_pk=Min('pk'))['min_pk']

def get_max_pk(model: Model): return model.objects.aggregate(Max('pk'))['pk__max']
    

    