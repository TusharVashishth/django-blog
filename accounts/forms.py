from django import forms
from django.core import validators
from .models import CustomUser
from django.forms import ModelForm
from django.shortcuts import get_object_or_404


class registerForm(forms.Form):
    name = forms.CharField(label='Name',
                           validators=[validators.MinLengthValidator(2), validators.MaxLengthValidator(30)],
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}))
    email = forms.CharField(label='Email', validators=[validators.EmailValidator()],
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}))
    password = forms.CharField(label='Password',
                               validators=[validators.MinLengthValidator(6), validators.MaxLengthValidator(40)],
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
    cpassword = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))

    def clean_cpassword(self):
        password = self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('cpassword')
        if password:
            if password != cpassword:
                raise forms.ValidationError('Confirm password not match')
            return cpassword

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = CustomUser.objects.filter(email=email)
        if len(user) > 0:
            raise forms.ValidationError('This email address already taken.')
        return email


class ProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone', 'image', 'facebook_url', 'instagram_url', 'twitter_url' ,'about']
        widgets = {
            'phone': forms.NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter phone number'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'facebook_url': forms.URLInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter facebook url'
            }),
            'instagram_url': forms.URLInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter instagram url'
            }),
            'twitter_url': forms.URLInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter twitter url'
            }),
            'about':forms.Textarea(attrs={
                'class':'form-control', 'placeholder':'Type about your self.'
            })

        }
