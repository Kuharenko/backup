from django.shortcuts import render, redirect
from forms import BlogForm
from PIL import Image, ImageFont, ImageDraw

# Create your views here.


def home(request):
    if request.POST:
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print form.errors
            return render(request, 'app/home.html', {"form": form})
    else:
        form = BlogForm()
        return render(request, 'app/home.html', {"form": form})