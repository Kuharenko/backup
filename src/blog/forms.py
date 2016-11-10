# -*- coding: utf8 -*-
from django import forms
from .models import Post, Comment, Category, Tags
from django.contrib.auth.models import User

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


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'password': forms.PasswordInput(attrs={'class': 'form-control'})
#         }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField()
