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
            'tages': forms.SelectMultiple(attrs={'class': 'form-control', 'required': False},)
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
        z = re.search('^([a-zA-Z0-9]+\s{0,1})+$', text)
        if len(text) < 2:
            raise forms.ValidationError("Длина сообщения не может быть меньше двух символов!")
        if z is None:
            raise forms.ValidationError("в сообщении должны быть буквы/цифры")
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

    def clean_tag_name(self):
        name = self.cleaned_data['tag_name']
        z = re.search('^([a-zA-Z]+\s{0,1})+$', name)

        # tags_array = []
        #
        # tags = str(name).split()
        # print name
        # for i in tags:
        #     match = re.match(r'^[A-Za-z]+$', i)
        #     if match:
        #         tags_array.append(i)
        #     else:
        #         raise forms.ValidationError("Тэги должны содержать только буквы!")
        if z is None:
            raise forms.ValidationError("Тэги должны содержать только буквы!")
        return name


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


class ChangePass(forms.Form):
    newpass = forms.CharField(widget=forms.PasswordInput)
    newpass2 = forms.CharField(widget=forms.PasswordInput)

    def clean_newpass(self):
        password = self.cleaned_data['newpass']
        z = re.search('^[a-zA-Z0-9]+$', password)
        if len(password) < 8:
            raise forms.ValidationError("Пароль должен содержать 8 символов и больше")

        if z is None:
            raise forms.ValidationError("только буквы/цифры")
        return password

    def clean_newpass2(self):
        password = self.cleaned_data['newpass2']
        z = re.search('^[a-zA-Z0-9]+$', password)
        if len(password) < 8:
            raise forms.ValidationError("Пароль должен содержать 8 символов и больше")
        if z is None:
            raise forms.ValidationError("только буквы/цифры")
        return password

    def clean(self):
        cleaned_data = super(ChangePass, self).clean()
        p1 = cleaned_data.get("newpass")
        p2 = cleaned_data.get("newpass2")

        if p1 == p2:
            return p1
        else:
            raise forms.ValidationError('Пароли не совпадают')


