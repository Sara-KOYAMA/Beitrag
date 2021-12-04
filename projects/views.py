from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from projects.models import Blog, Comment
from django.utils import timezone
from django.utils.timezone import localtime
from django.http import Http404
import re

# Create your views here.
def home(request):
    return render(request, 'projects/home.html', {})

def create_user(request):
    User = get_user_model()
    if request.method=='POST': # 登録
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if re.search('@iniad.org', email):
            user = User.objects.create_user(name, email, password)
            user.save()
            return redirect('home')
        
        return redirect('error')
    return render(request, 'registration/create.html', {})

def login(request):
    return render(request, 'registration/login.html', {})

def error(request):
    return render(request, 'registration/error.html', {})

@login_required
def create_message(request):
    if request.method=='POST':
        blog=Blog.objects.create(
            title=request.POST['title'],
            text=request.POST['text'],
            date=localtime(timezone.now())
        )
        blog.save()
        return redirect('list')

    return render(request, 'projects/message.html')

@login_required
def list(request):
    blog= Blog.objects.all()
    
    if request.method == 'POST':
        blog = Blog(title=request.POST['title'], text=request.POST['text'], posted_at=timezone.now())
        blog.save()
    blog = Blog.objects.order_by('-date')

    context = {
        'blog': blog
    }
    return render(request, 'projects/list.html', context) 

@login_required
def detail(request, blog_id):
    try:
        blog= Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    
    if request.method == 'POST':
        comment=Comment.objects.create(
            comment=blog,
            text=request.POST['text'],
            posted_at=localtime(timezone.now())
        )
        comment.save()
    
    context = {
        'blog': blog,
        'comments': blog.comments.all().order_by('-posted_at')
    }
    
    return render(request, 'projects/detail.html', context)

@login_required
def edit(request, blog_id):
    try : 
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")

    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.text= request.POST['text']
        blog.save()
        return redirect('list')

    context = {
        'blog': blog
    }
    return render(request, 'projects/edit.html', context)

@login_required
def delete(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    
    blog.delete()
    return redirect(list)

@login_required
def delete_comment(request, comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        raise Http404("Comment does not exist")
    blog_id = comment.comment.id
    comment.delete()
    return redirect(detail, blog_id)

@login_required
def edit_comment(request, comment_id):
    try : 
        comment = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        raise Http404("Comment does not exist")

    if request.method == 'POST':
        comment.text= request.POST['text']
        blog_id = comment.comment.id
        comment.save()
        return redirect(detail, blog_id)

    context = {
        'comment': comment
    }
    return render(request, 'projects/edit_comment.html', context)