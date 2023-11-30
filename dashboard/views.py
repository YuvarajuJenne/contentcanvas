from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from app.models import Category,Blog
from dashboard.forms import CategoryForm, PostForm
from django.template.defaultfilters import slugify
from django.contrib import auth

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count=Category.objects.all().count()
    blog_count=Blog.objects.all().count()
    context={
        'category_count':category_count,
        'blog_count':blog_count,
    }
    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html')

def add_category(request):
    if request.method=='POST':
       form=CategoryForm(request.POST) 
       if form.is_valid():
          form.save()
          return redirect('categories')
    form=CategoryForm()
    context={
        'form':form,
    }
    return render(request,'dashboard/add_category.html',context)

def edit_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    if request.method=='POST':
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
        return redirect('categories')
    form=CategoryForm(instance=category)
    context={
        'form':form,
    }
    return render(request,'dashboard/edit_category.html',context)

def delete_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')

def posts(request):
    post=Blog.objects.all()
    context={
        'post':post,
    }   
    return render(request,'dashboard/posts.html',context)

def add_posts(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            title=form.cleaned_data['title']
            post.slug=slugify(title)
            post.save()
            return redirect('posts')
    form=PostForm()
    context={
        'form':form,
    }
    return render(request,'dashboard/add_posts.html',context)

def edit_posts(request,pk):
    post=get_object_or_404(Blog,pk=pk)
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():  
            post=form.save()
            title=form.cleaned_data['title']
            post.slug=slugify(title)
            post.save()
            return redirect('posts')
    form=PostForm(instance=post)
    context={
        'form':form,
        'post':post,
    }
    return render(request,'dashboard/edit_posts.html',context)

def delete_posts(request,pk):
    post=get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')

def logout(request):
    auth.logout(request)
    return redirect('home')