from django.db import models

# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    post_views = models.IntegerField(default=0)
    post_category = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.post_category}: {self.post_title} created at {self.created_at}"


