from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=100, blank=True,default='')

    def save(self, *args, **kwargs):

        self.slug = slugify(f"{self.title} + {self.content[1:5]}") 
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.category}: {self.title} created at {self.created_at} {self.slug}"


class Users(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    comment = models.TextField(default='')


