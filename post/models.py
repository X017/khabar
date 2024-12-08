from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return f" {self.category} "


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #Foreing Key to Category


    def __str__(self):
        return f"{self.category}: {self.title} created at {self.created_at}"


