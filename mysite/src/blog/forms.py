# -*- coding: utf8 -*-
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
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
        # first call parent's constructor
        super(CommentForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['author'].required = True
