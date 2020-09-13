from django.forms import ModelForm
from .models import Blog, Comment
from django import forms


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['user', 'heading', 'sub_heading', 'time_to_read', 'body', 'image', 'is_private']
        widgets = {
            'heading': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter heading'
            }),
            'sub_heading': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter sub heading'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'is_private': forms.Select(attrs={
                'class': 'form-control'
            }),
            'time_to_read': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter time to read in minutes'
            }),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'user' ,'blog']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Leave your comment'
            })
        }
