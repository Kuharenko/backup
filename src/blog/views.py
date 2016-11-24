# -*- coding: utf8 -*-

from django.utils import timezone
from blog.forms import *
from blog.models import Post, Comment, Category, Tags, ClickLike
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from annoying.decorators import render_to
from django.contrib.auth.hashers import make_password


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


@render_to('blog/adminka.html')
@permission
def adminka(request):
    request.user.is_authenticated()
    posts = Post.objects.all()
    return {'posts': posts}


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
            return HttpResponse(200)
    return HttpResponse(400)


@render_to('blog/search.html')
def select_all_posts(request):
    posts = Post.objects.filter().order_by('-datetime').all()
    comments = Comment.objects.all()
    paginator = Paginator(posts, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return {'posts': posts, 'comments': comments}


@render_to('blog/post_detail.html')
def view_post(request, post_id):
    post = get_object_or_404(Post or None, pk=post_id)
    comment_form = CommentForm(request.POST or None)
    if not request.session.get('views'):
        request.session['views']=True
        request.session.set_expiry(3000)
        post.views_count += 1
        post.save()
    if request.POST:
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.created_date = timezone.now()
            comment.author = request.user
            comment.save()
            return redirect(request.path)
    return {'post': post, 'comment_form': comment_form}


@login_required
@render_to('blog/post_edit.html')
def post_new(request):
    post_add_form = PostForm(request.POST or None)
    if request.POST:

        cats = []
        tags = []

        for a in request.POST.getlist('category'):
            cats.append(int(a))
        for a in request.POST.getlist('tages'):
            tags.append(int(a))

        if post_add_form.is_valid():
            post = post_add_form.save(commit=False)
            post.datetime = timezone.now()
            post.save()

            post.category = cats
            post.tages = tags
            post.save()
            return redirect('post_detail', post_id=post.pk)
    return {'post_add_form': post_add_form}


@login_required
@render_to('blog/post_edit.html')
def post_edit(request, post_id):

    if 'edit' in request.POST:
        post = get_object_or_404(Post, pk=post_id)
        post_form = PostForm(request.POST or None, instance=post)
        if request.POST:
            cats = []
            tags = []

            for categories in request.POST.getlist('category'):
                cats.append(int(categories))
            for tages in request.POST.getlist('tages'):
                tags.append(int(tages))

            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.datetime = timezone.now()
                post.category = cats
                post.tages = tags
                post.save()
                return redirect('post_detail', post_id=post.pk)
        return {'post_add_form': post_form}
    elif 'delete' in request.POST:
        instance = Post.objects.get(id=post_id)
        instance.delete()
        return redirect('admin')


@login_required
def post_delete(request, post_id):
    instance = Post.objects.get(id=post_id)
    instance.delete()
    return HttpResponse(200)
        #redirect('admin')


@login_required
@render_to('blog/tags_add.html')
def add_tag(request):
    tag_form = TagsForm(request.POST or None)
    if request.POST:
        if tag_form.is_valid():
            tags = str(request.POST.get('tag_name')).split()
            for i in tags:
                tag = Tags()
                match = re.match(r'^[A-Za-z]+$', i)
                if match:
                    tag.tag_name = i
                    try:
                        tag.save()
                    except:
                        pass
            return redirect('post_new')
    return {'tag_form': tag_form}


@login_required
@render_to('blog/category_add.html')
def add_category(request):
    category_form = CategoryForm(request.POST or None)
    if request.POST:
        if category_form.is_valid():
            cat = category_form.save(commit=False)
            cat.save()
            return redirect('post_new')
    return {'category_form': category_form}


@render_to('blog/comment_list.html')
def comments_list(request):
    comments = Comment.objects.all()
    return {'comments': comments}


@render_to('blog/category_list.html')
def category_list(request):
    categories = Category.objects.all()
    return {'categories': categories}


@login_required
@render_to('blog/category_edit.html')
def category_edit(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category_form = CategoryForm(request.POST or None, instance=category)
    if request.method == "POST":
        if category_form.is_valid():
            cat = category_form.save(commit=False)
            cat.save()
            return redirect('post_new')
    return {'category_form': category_form}


@login_required
@render_to('blog/comm_edit.html')
def comment_edit(request, post_id, comment_id):
    comm = get_object_or_404(Comment, pk=comment_id)
    comment_form = CommentForm(request.POST or None, instance=comm)
    if request.method == "POST":
        if comment_form.is_valid():
            comm = comment_form.save(commit=False)
            comm.datetime = timezone.now()
            comm.save()
            return redirect('post_detail', post_id=post_id)
    return {'comment_form': comment_form}


@login_required
def comment_delete(request, post_id, comment_id):
    instance = Comment.objects.get(pk=comment_id)
    instance.delete()
    return redirect('post_detail', post_id=post_id)


@isSu
def cat_delete(request, category_id):
    instance = Category.objects.get(id=category_id)
    instance.delete()
    return redirect('category_list')


@render_to('blog/search_by_category.html')
def search_by_category(request, category_id):
    posts_with_category = Post.objects.filter(category=category_id).order_by('-datetime').all()
    return {'posts_with_category': posts_with_category}


@render_to('blog/search_by_tag.html')
def search_by_tag(request, tag_id):
    posts_with_tag = Post.objects.filter(tages=tag_id).order_by('-datetime').all()
    return {'posts_with_tag': posts_with_tag}


@render_to('blog/register.html')
def register(request):
    registration_form = RegisterForm(request.POST or None)
    if request.POST:
        if registration_form.is_valid():
            usr = registration_form.save(commit=False)
            usr.password = make_password(request.POST.get('password'))
            usr.save()
            return redirect('list')
    return {'registration_form': registration_form}


@render_to('blog/login.html')
def log_in(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('/blog/')
    return {}


@login_required
def logout(request):
    auth.logout(request)
    return redirect('list')


@login_required
@render_to('blog/change_password.html')
def change_pass(request):
    change_pass_form = ChangePass(request.POST or None)
    if request.POST:
        user = User.objects.get(username=request.user.username)
        if change_pass_form.is_valid():
            user.set_password(request.POST.get('newpass'))
            user.save()
            logout(request)
            return redirect('login')
    return {'change_pass_form': change_pass_form}


def custom_404(request):
    return render(request, '404.html')