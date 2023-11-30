from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='categories'
    def __str__(self):
        return self.category
    
choices={
    ('draft','draft'),
    ('published','published')
}

class Blog(models.Model):
    title=models.CharField( max_length=100)
    slug=models.CharField( max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/%y/%m/%d')
    short_description=models.TextField(max_length=1000)
    blog=models.TextField(max_length=10000)
    status=models.CharField(max_length=100,choices=choices,default='draft')
    is_featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)