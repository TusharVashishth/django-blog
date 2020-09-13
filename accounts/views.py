from django.shortcuts import render, redirect
from .forms import registerForm, ProfileForm
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth import login, authenticate, logout


def userRegister(request):
    form = registerForm()
    context = {'form': form}
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            CustomUser.objects.create_user(name=name, email=email, password=password)
            messages.success(request, 'Account created successfully.')
            return redirect('login')
        else:
            context = {'form': form}
            return render(request, 'accounts/register.html', context)
    return render(request, 'accounts/register.html', context)


def userLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'accounts/login.html')


def userLogOut(request):
    logout(request)
    messages.success(request, 'Successfully logout.')
    return redirect('login')


def userProfile(request):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(id=request.user.id)
        form = ProfileForm(instance=user)
        context = {'form': form}
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request ,'Profile updated successfully.')
                return redirect('profile')
            else:
                context = {'form': form}
                return render(request, 'dashboard/profile.html', context)
    else:
        messages.error(request, 'Please login first.')
        return redirect('login')
    return render(request, 'dashboard/profile.html', context)
