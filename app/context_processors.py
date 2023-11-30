from django.shortcuts import redirect
from app.models import Category
from social.models import socialLinks
def get_categories(request):
    categories=Category.objects.all()
    return dict(categories=categories)

def get_sociallinks(request):
    sociallinks=socialLinks.objects.all()
    return dict(sociallinks=sociallinks)