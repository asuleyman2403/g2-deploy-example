from django.shortcuts import render, redirect
from blogs.models import Blog, Post
from blogs.forms import CreateBlogForm, CreatePostForm


def home_page(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(owner_id=request.user.id).order_by('-created_at')
        return render(request, 'blogs/index.html', {'blogs': blogs})
    else:
        return redirect('/auth/login/')


def create_blog(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = CreateBlogForm()
            return render(request, 'blogs/create-blog.html', {'form': form})
        if request.method == 'POST':
            form = CreateBlogForm(request.POST)
            if form.is_valid():
                title = form.data.get('title')
                description = form.data.get('description')
                blog = Blog(title=title, owner_id=request.user.id)
                blog.save()
                return redirect('/')
            else:
                return render(request, 'blogs/create-blog.html', {'form': form})
    else:
        return redirect('/auth/login/')


def blog_details(request, pk):
    if request.user.is_authenticated:
        if request.method == 'GET':
            blog = Blog.objects.get(id=pk)
            posts = Post.objects.filter(blog_id=pk).order_by('-created_at')
            form = CreatePostForm()
            return render(request, 'blogs/blog-details.html', {'blog': blog, 'form': form, 'posts': posts})
        if request.method == 'POST':
            form = CreateBlogForm(request.POST)
            if form.is_valid():
                title = form.data.get('title')
                description = form.data.get('description')
                blog = Blog(title=title, description=description, owner_id=request.user.id)
                blog.save()
                return redirect('/')
            else:
                return render(request, 'blogs/create-blog.html', {'form': form})
    else:
        return redirect('/auth/login/')


def create_post(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            blog = Blog.objects.get(id=pk)
            if request.user.id == blog.owner.id:
                form = CreatePostForm(request.POST, request.FILES)
                if form.is_valid():
                    title = form.data.get('title')
                    content = form.data.get('content')
                    image = form.files.get('image')
                    post = Post(title=title, content=content, blog_id=blog.id, image=image)
                    post.save()
                    return redirect('/blogs/' + str(blog.id) + '/')
                else:
                    posts = Post.objects.filter(blog_id=pk).order_by('-created_at')
                    return render(request, 'blogs/blog-details.html', {'blog': blog, 'form': form, 'posts': posts})
    return redirect('/')


def post_details_page(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(id=pk)
        return render(request, 'blogs/post-details.html', {'post': post})
    return redirect('/auth/login/')


def delete_blog(request, pk):
    if request.user.is_authenticated:
        blog = Blog.objects.get(id=pk)
        if blog.owner.id == request.user.id:
            blog.delete()
            return redirect('/')
        return redirect('/')


def delete_post(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(id=pk)
        if post.blog.owner.id == request.user.id:
            post.delete()
            return redirect('/blogs/' + str(post.blog.id) + '/')
        return redirect('/')
