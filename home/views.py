from django.shortcuts import render, redirect
from .models import Post
from .forms import CreatePost, UpdatePost
from django.contrib import messages
# Create your views here.

def HomeView(request):
    return render(request, 'home/index.html')

def AboutView(request):
    return render(request, 'home/about.html')

def ContactView(request):
    return render(request, 'home/contact.html')

def PoststView(request):
    all_posts = Post.objects.all().order_by('-created')
    return render(request, 'home/posts.html', {'posts':all_posts})

def DetailstView(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'home/details.html', {'post':post})

def CreatePostView(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Post.objects.create(title=cd['title'],author=cd['author'],body=cd['body'],created=cd['created'])
            return redirect('home:posts')
    else:
        form = CreatePost()
    return render(request,'home/create.html',{'form':form})

def DeletePostView(request, post_id):
    post = Post.objects.get(pk=post_id).delete()
    return redirect('home:posts')

def UpdatePostView(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = UpdatePost(request.POST,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post successfully update','success')
            return redirect('home:posts')
    else:
        form = UpdatePost(instance=post)
    return render(request, 'home/update.html',{'form':form})