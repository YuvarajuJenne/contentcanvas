from django import forms
from app.models import Category,Blog

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','category','image','short_description','blog','status','is_featured')