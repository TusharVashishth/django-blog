from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BlogForm, CommentForm
from .models import Blog, Comment


def home(request):
    blogs = Blog.objects.filter(is_private='0')
    context = {'blogs': blogs}
    return render(request, 'blog/index.html', context)


def dashboard(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.all().filter(user_id=request.user.id).order_by('-created_at')
        context = {'blogs': blogs}
        return render(request, 'dashboard/index.html', context)
    else:
        messages.error(request, 'Please login first')
        return redirect('login')


def addBlog(request):
    if request.user.is_authenticated:
        form = BlogForm()
        context = {'form': form}
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post Added successfully.')
                return redirect('dashboard')
            else:
                print("else Part")
                context = {'form': form}
                return render(request, 'dashboard/addBlog.html', context)
        return render(request, 'dashboard/addBlog.html', context)
    else:
        messages.error(request, 'Please login first.')
        return redirect('login')


def updateBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)
    context = {'form': form}
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Updated successfully.')
            return redirect('dashboard')
        else:
            context = {'form': form}
            return render(request, 'dashboard/addBlog.html', context)
    return render(request, 'dashboard/addBlog.html', context)


def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    messages.success(request, 'Blog Deleted successfully.')
    return redirect('dashboard')


def singleBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    comments = Comment.objects.filter(blog_id=pk)
    form = CommentForm()
    context = {'blog': blog, 'form': form, 'comments': comments}
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Comment post successfully.')
                return redirect('single-blog', pk)
            else:
                print('else part')
                return render(request, 'blog/blog_single.html', context)
        else:
            messages.error(request, 'Please login first')
            return redirect('login')
    return render(request, 'blog/blog_single.html', context)


def articals(request):
    blogs = Blog.objects.all().order_by('-id')
    context = {'blogs': blogs}
    return render(request, 'blog/articals.html', context)
