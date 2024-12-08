from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return f" {self.category} "

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='None')  # Foreign Key to Category
    slug = models.SlugField(unique=True, max_length=100, default=None)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category}: {self.title} created at {self.created_at}"
