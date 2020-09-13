from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('dashboard/', dashboard, name="dashboard"),
    path('add-blog/', addBlog, name="add-blog"),
    path('updated-blog/<str:pk>/', updateBlog, name="update-blog"),
    path('delete-blog/<str:pk>/', deleteBlog, name="delete-blog"),
    path('single-blog/<str:pk>/', singleBlog, name="single-blog"),
    path('articals/', articals, name="articals"),
]
