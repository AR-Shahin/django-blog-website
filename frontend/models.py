from django.db import models

class Slider(models.Model):
    id = models.AutoField(primary_key=True,name="id",unique=True)
    title = models.CharField(max_length=100,name="title")
    order = models.IntegerField(name="order",default=0)
    status = models.BooleanField(name="status",default=True)
    content = models.TextField(name="content")
    image = models.ImageField(name="image",upload_to='images/sliders/')


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
    slug = models.CharField(max_length=100,name="slug",unique=True,primary_key=True)
    view = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    image = models.ImageField(name="image",upload_to='images/posts/',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()



    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
        managed = True
        verbose_name = 'Post'
        verbose_name_plural = 'posts'
