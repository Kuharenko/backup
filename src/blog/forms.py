# -*- coding: utf8 -*-
from django import forms
from .models import Post, Comment, Category, Tags
from django.contrib.auth.models import User
import re


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'tages')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control', 'required': False}),
            'tages': forms.SelectMultiple(attrs={'class': 'form-control', 'required': False})
        }

    def clean_title(self):
        text = self.cleaned_data['title']
        z = re.search('^[a-zA-Z]+$', text)
        if z is None:
            raise forms.ValidationError("Заголовок должен содержать только буквы!")
        return text


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        fields = ('author', 'text')
        labels = {
            'author': 'Author',
            'text': 'Message',
        }
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['author'].required = False

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 2:
            raise forms.ValidationError("Длина сообщения не может быть меньше двух символов!")
        return text


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', 'category_description')
        labels = {
            'category_name': 'Название категории',
            'category_description': 'Короткое описание',
        }
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
            'category_description': forms.Textarea(attrs={'class': 'form-control'})
        }


class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['tag_name'#, 'tag_description'
        ]
        labels = {
            'tag_name': 'Название тэгов',
            #'tag_description': 'Описание тэга'
        }
        widgets = {
            'tag_name': forms.TextInput(attrs={'class': 'form-control'}),
           # 'tag_description': forms.Textarea(attrs={'class': 'form-control'})
        }


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Пользователь',
            'password': 'Пароль'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }

    def clean_username(self):
        name = self.cleaned_data['username']
        z = re.search('^[a-zA-Z0-9]+$', name)
        if z is None:
            raise forms.ValidationError("Имя пользователя может содержать только буквы и цифры!")
        return name


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.PasswordInput()

