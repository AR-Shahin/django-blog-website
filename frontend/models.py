from PIL import Image 
from django.db import models
from django.forms import ValidationError
from django.utils.text import slugify

class Slider(models.Model):
    id = models.AutoField(primary_key=True,name="id",unique=True)
    title = models.CharField(max_length=100,name="title")
    order = models.IntegerField(name="order",default=0)
    status = models.BooleanField(name="status",default=True)
    content = models.TextField(name="content")
    image = models.ImageField(name="image",upload_to='images/sliders/')


    def __str__(self):
        return self.title + " <-> " + str(self.order)

    class Meta:
        db_table = 'sliders'
        managed = True
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'
        
class Category(models.Model):
    title = models.CharField(max_length=100,name="title")
    slug = models.CharField(max_length=100,name="slug")
    image = models.ImageField(name="image",upload_to='images/category/',null=True, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'categories'
        
class SubCategory(models.Model):
    title = models.CharField(max_length=100,name="title")
    slug = models.CharField(max_length=100,name="slug")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="sub_categories")


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'sub_categories'
        managed = True
        verbose_name = 'Sub Category'
        verbose_name_plural = 'sub_categories'
        
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="posts")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE,related_name="posts",null=True)
    tags = models.ManyToManyField(Tag,related_name="posts")
    title = models.CharField(max_length=100,name="title",unique=True)
    slug = models.SlugField(max_length=100,name="slug",unique=True)
    view = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    image = models.ImageField(name="image",upload_to='images/posts/',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    trending = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # Automatically generate a slug based on the title
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def clean(self):
        super().clean()
        image = self.image

        # Check if the uploaded file is an image
        if not image.name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            raise ValidationError('Only JPG, JPEG, PNG, and GIF files are allowed.')

        # Check if the image dimensions are within a certain range
        img = Image.open(image)
        if img.width > 1000 or img.height > 1000:
            raise ValidationError('Image dimensions should be 1000x1000 pixels or less.')


    class Meta:
        db_table = 'posts'
        managed = True
        verbose_name = 'Post'
        verbose_name_plural = 'posts'


class Contact(models.Model):
    
    name = models.CharField(name="name",max_length=200,)
    email = models.EmailField(name="email")
    subject = models.CharField(name="subject",max_length=200,)
    status = models.BooleanField(name="status",default=False)
    message = models.TextField(name="message")
    class Meta:
        db_table = 'contacts'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'contacts'
        
    def __str__(self):
        return self.subject