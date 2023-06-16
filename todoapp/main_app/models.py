from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# # Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    subtask = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if not self.image_url:
            # Generate the random image URL using the Lorem Picsum API
            self.image_url = 'https://picsum.photos/200/300'  # Example URL
        super().save(*args, **kwargs)

    def __str__(self):
      return self.title
    
    class Meta:
        ordering = ['complete']
        
class SubTask(models.Model):
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks', default=1)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
      

