#coding: utf-8

from django.shortcuts import render, redirect,get_object_or_404
from django.utils import timezone
from .forms import PostForm
from blog.models import Post 
from django.views.generic import ListView, DetailView
# Create your views here.

def index(request):
	return render(request,'blog/index.html',{})



class PostsListView(ListView): # представление в виде списка
    model = Post                   # модель для представления 

class PostDetailView(DetailView): # детализированное представление модели
    model = Post

def post_new(request):
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

def post_edit(request, pk):
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

def post_delete(request, pk):
		instance = Post.objects.get(id=pk)
		instance.delete()
		return redirect('list')