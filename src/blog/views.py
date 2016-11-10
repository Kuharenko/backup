# -*- coding: utf8 -*-


import re
from django.utils import timezone
from blog.forms import *
from blog.models import Post, Comment, Category, Tags, ClickLike
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth


def permission(decorate):
    def wrapper(request):
        if request.user.is_anonymous():
            return render(request, 'blog/deny.html')
        else:
            if request.user.is_superuser:
                return decorate(request)
    return wrapper


def isSu(decorate):
    def wrapper(request, pk, *rk):
        if request.user.is_superuser:
            return decorate(request, pk, *rk)
        else:
            return render(request, 'blog/deny.html')
    return wrapper


@permission
def adminka(request):
    posts = Post.objects.all()
    return render(request, 'blog/adminka.html', {'posts': posts})


def index(request):
    return render(request, 'blog/post_list.html')


def add_like(request, pk):
    try:
        cl = ClickLike.objects.get(user=request.user.id, post=pk)
    except ClickLike.DoesNotExist:
        if request.user.id:
            article = get_object_or_404(Post, pk=pk)
            article.likes_count += 1
            cl = ClickLike.objects.create(post=article, user=request.user.id)
            cl.save()
            article.save()
            return redirect(request.GET.get('next', '/'))
        else:
            return redirect(request.GET.get('next', '/'))
    return redirect(request.GET.get('next', '/'))


def PostsListView(request):
    post = Post.objects.filter().order_by('-datetime').all()
    comment = Comment.objects.all()
    paginator = Paginator(post, 5)

    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    return render(request, 'blog/search.html', {'post': post, 'comm': comment})


def select_all_posts(request):
    post = Post.objects.all()
    return render(request, 'blog/search.html', {'list': post})


def view_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST or None)
    post.views_count += 1
    post.save()
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.created_date = timezone.now()
        comment.author = request.user
        comment.save()
        return redirect(request.path)
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})


@isSu
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        cats = []
        tags = []

        for a in request.POST.getlist('category'):
            cats.append(int(a))
        for a in request.POST.getlist('tages'):
            tags.append(int(a))

        if form.is_valid():
            post = form.save(commit=False)
            post.datetime = timezone.now()
            post.save()

            post.category = cats
            post.tages = tags
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            print form.errors
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@isSu
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        cats = []
        tags = []

        for a in request.POST.getlist('category'):
            cats.append(int(a))
        for a in request.POST.getlist('tages'):
            tags.append(int(a))

        if form.is_valid():
            post = form.save(commit=False)
            post.datetime = timezone.now()
            post.category = cats
            post.tages = tags
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            print form.errors
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@isSu
def post_delete(request, pk):
    instance = Post.objects.get(id=pk)
    instance.delete()
    return redirect('admin')


def add_tag(request):
    if request.user.is_anonymous():
        return render(request, 'blog/deny.html')
    else:
        form = TagsForm(request.POST or None)
        if form.is_valid():
            tags = str(request.POST.get('tag_name')).split()
            for i in tags:
                tag = Tags()
                match = re.match(r'^[A-Za-z]+$', i)
                print match
                if match:
                    tag.tag_name = i
                    try:
                        tag.save()
                    except:
                        pass
            return redirect('post_new')
    return render(request, 'blog/tags_add.html', {'form': form})


@permission
def add_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        cat = form.save(commit=False)
        cat.save()
        return redirect('post_new')
    return render(request, 'blog/category_add.html', {'form': form})


def comments_list(request):
    comments = Comment.objects.all()
    return render(request, 'blog/comment_list.html', {'list': comments})


def about(request):
    return render(request, 'blog/about.html', {})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'list': categories})


@isSu
def category_edit(request, pk):
    comm = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=comm)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.save()
            return redirect('post_new')
    else:
        form = CategoryForm(instance=comm)
    return render(request, 'blog/category_edit.html', {'form': form})


@isSu
def comment_edit(request, pk):

    comm = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comm)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.datetime = timezone.now()
            comm.save()
            return redirect('post_detail', pk=comm.pk)
    else:
        form = CommentForm(instance=comm)
    return render(request, 'blog/comm_edit.html', {'form': form})


@isSu
def comment_delete(request, pk, rk):
    instance = Comment.objects.get(id=pk)
    instance.delete()
    return redirect('post_detail', pk=rk)


@isSu
def cat_delete(request, pk):
    instance = Category.objects.get(id=pk)
    instance.delete()
    return redirect('category_list')


def search_by_category(request, pk):
    return render(request, 'blog/search.html', {'post': Post.objects.filter(category=pk).order_by('-datetime').all()})


def search_by_tag(request, pk):
    return render(request, 'blog/search.html', {'post': Post.objects.filter(tages=pk).order_by('-datetime').all()})


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        usr = form.save(commit=False)
        usr.save()
        print 'User registered!'+request.POST.get('username')
        return redirect('list')
    return render(request, 'blog/register.html', {'form': form})


def log_in(request):
    # u = request.POST.get('username')
    # p = request.POST.get('password')
    #
    # user = auth.authenticate(username=u, password=p)
    # print 'user ',u
    # print 'pass ',p
    # if user is not None and user.is_active:
    #     auth.login(request, user)
    #     return redirect("list")
    # else:
    #     return redirect('login')

    form = LoginForm(request.POST or None)
    print request.POST.get('username')
    print request.POST.get('password')
    if form.is_valid():
        user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None and user.is_activate:
            auth.login(request, request.POST.get('username'))
            return redirect('list')
        else:
            print 'Error'
            return redirect('/blog/')
    else:
        print form.errors
    return render(request, 'blog/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('list')