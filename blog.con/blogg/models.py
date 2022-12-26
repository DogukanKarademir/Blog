from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50, null=True)

class Blog(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'),
    )
    title = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=400)
    keywords = models.CharField(blank=True, max_length=200)
    image = models.ImageField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
   
    detail = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    
    def __str__(self):
        return self.title