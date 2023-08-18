from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=100,name="title")
    content = models.TextField(name="content")
    image = models.ImageField(name="image")


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'sliders'
        managed = True
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'
