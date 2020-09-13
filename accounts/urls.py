from django.urls import path
from .views import userRegister, userLogin, userLogOut, userProfile

urlpatterns = [
    path('register/', userRegister, name="register"),
    path('login/', userLogin, name="login"),
    path('logout/', userLogOut, name="logout"),
    path('profile/', userProfile, name="profile"),
]
