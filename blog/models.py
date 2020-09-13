from django.db import models
from accounts.models import CustomUser
from ckeditor.fields import RichTextField
from django.core import validators


class Blog(models.Model):
    Private = (
        (0, 'no'),
        (1, 'yes'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    heading = models.CharField(validators=[validators.MinLengthValidator(10)], max_length=300, null=True)
    sub_heading = models.CharField(validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(15)],
                                   max_length=300, null=True)
    time_to_read = models.CharField(max_length=100, null=True)
    body = RichTextField(max_length=5000, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    is_private = models.IntegerField(default=0, choices=Private, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sub_heading


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    message = models.TextField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name
