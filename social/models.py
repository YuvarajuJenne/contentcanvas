from django.db import models

# Create your models here.
class socialLinks(models.Model):
    flatform=models.CharField(max_length=100)
    link=models.URLField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.flatform