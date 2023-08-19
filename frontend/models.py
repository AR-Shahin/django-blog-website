from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=100,name="title")
    content = models.TextField(name="content")
    image = models.ImageField(name="image",upload_to='images/')


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'sliders'
        managed = True
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'
        
class Category(models.Model):
    title = models.CharField(max_length=100,name="title")
    slug = models.CharField(max_length=100,name="slug")


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'categories'
        
class Tag(models.Model):
    name = models.CharField(max_length=100,name="name")
    slug = models.CharField(max_length=100,name="slug")


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'
        managed = True
        verbose_name = 'Tag'
        verbose_name_plural = 'tags'
        
        
class Post(models.Model):
    title = models.CharField(max_length=100,name="title")
    slug = models.CharField(max_length=100,name="slug")
    view = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
        managed = True
        verbose_name = 'Post'
        verbose_name_plural = 'posts'
