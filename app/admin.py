from django.contrib import admin
from app.models import Category,Blog

# Register your models here.

class blogadmin(admin.ModelAdmin):
    prepopulated_fields={
        'slug':('title',)
    }
    search_fields=('title','id','category__category','status','is_featured')
    list_display=('title','id','status','is_featured')
    list_editable=('status','is_featured')

admin.site.register(Category)
admin.site.register(Blog,blogadmin)