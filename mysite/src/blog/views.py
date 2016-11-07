# -*- coding: utf8 -*-

from django.shortcuts import render
from django.utils import timezone
from .forms import PostForm, CommentForm
from blog.models import Post, Comment, Category, Tags, TagToPost
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext


def index(request):
    return render(request, 'blog/post_list.html', {})


class PostsListView(ListView):  # представление в виде списка
    model = Post


class PostDetailView(DetailView):  # детализированное представление модели
    model = Post


def adminka(request):
    if request.user.is_anonymous():
        return render(request, 'blog/deny.html')
    else:
        if request.user.is_superuser:
            posts = Post.objects.all()
            return render(request, 'blog/adminka.html', {'posts': posts})
        else:
            return render(request, 'blog/deny.html')


def view_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.created_date = timezone.now()
        comment.save()
        return redirect(request.path)
    form.initial['author'] = request.user
    return render_to_response('blog/post_detail.html',
                              {
                                  'post': post,
                                  'form': form,
                              },
                              context_instance=RequestContext(request))


def post_new(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.datetime = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        return render(request, 'blog/deny.html')


def post_edit(request, pk):
    if request.user.is_superuser:
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.datetime = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        return render(request, 'blog/deny.html')


def post_delete(request, pk):
    if request.user.is_superuser:
        instance = Post.objects.get(id=pk)
        instance.delete()
        return redirect('admin')
    else:
        return render(request, 'blog/deny.html')


class CommentsListView(ListView):
    model = Comment


def about(request):
    return render(request, 'blog/about.html', {})


def comment_edit(request, pk):
    if request.user.is_superuser:
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
    else:
        return render(request, 'blog/deny.html')

#КАКАШКА!!!!


def comment_delete(request, pk, rk):
    if request.user.is_superuser:
        instance = Comment.objects.get(id=pk)
        instance.delete()
        return redirect('post_detail', pk=rk)
    else:
        return render(request, 'blog/deny.html')