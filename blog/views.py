
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Post,Comments
from django.contrib import messages
import random

slug=0

def index(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        if len(query) > 75 or query == "":
            posts = Post.object.none()
        else:
            post_title = Post.objects.filter(title__icontains=query)
            post_content = Post.objects.filter(content__icontains=query)
            post_author = Post.objects.filter(author__icontains=query)
            posts = (post_title.union(post_content)).union(post_author)

        context = {'posts': posts, 'num_posts': len(posts)}
        return render(request, 'bloghome.html', context)

    posts = Post.objects.all()
    context = {'posts': posts, 'num_posts': len(posts)}
    return render(request, 'bloghome.html', context)


def write(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        slug = str(random.randint(100, 1000000))
        content = request.POST.get('content')
        author = request.user.username
        post = Post(author=author, title=title, slug=slug, content=content)
        post.save()
        messages.success(request, "Blog posted successfully.")
        return redirect("BlogHome")
    else:
        return render(request, 'writeblog.html')


def viewblog(request, slug):
    flag=True
    post = Post.objects.filter(slug=slug).first()
    comments=Comments.objects.filter(post=post)
    if  post.author != str(request.user.username):
        flag=False
    return render(request, 'blogpost.html', {'post': post,'comments':comments,'flag':flag})


def showmyblog(request):
    myPosts = Post.objects.filter(author=request.user.username)
    context = {'posts': myPosts, 'num_posts': len(myPosts)}
    print(context)
    return render(request, 'myblogs.html', context)

def write_comment(request):
    if request.method=='POST':
        content=request.POST.get('content')
        post_id=request.POST.get('post_id')
        post=Post.objects.get(post_id=post_id)
        if content=="":
            return redirect(f"/blog/{post.slug}")
        com=Comments(content=content,author=request.user,post=post)
        com.save()
        comments=Comments.objects.filter(post=post)
        messages.success(request,"Comment posted successfully")
        return render(request, 'blogpost.html', {'post': post,'comments':comments})
    return render(request,"/")

def edit(request):
    if request.method=='POST':
        slug=request.POST.get('slug')
        content=request.POST.get('content')
        return render(request,'editblog.html',{'content':content,'slug':slug})
    return render(request,'editblog.html',{'content':content,'slug':slug})


def editblog(request):
    if request.method=='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user.username
        slug=request.POST.get('slug')
        post=Post.objects.filter(slug=slug)[0]
        post.content=content
        post.save()
        return redirect("BlogHome")
    else:
        return HttpResponse("Please follow protocol")

def delete(request):
    if request.method=='POST':
        slug=request.POST.get('slug')
        title=request.POST.get('title')
    return render(request,'delete.html',{'slug':slug,'title':title})

def deleteblog(request):
    if request.method=='POST':
        slug=request.POST.get('slug')
        post=Post.objects.filter(slug=slug)[0]
        post.delete()
        messages.success(request,"Post Deleted Successfully.")
        return redirect("BlogHome")
    else:
        return HttpResponse("Bad Pathway")