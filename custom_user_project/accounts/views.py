from django.contrib.auth import login
from .models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']

        # Create a new user
        user = CustomUser.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password)
        login(request, user)
        return redirect('signup_success')

    return render(request, 'signup.html')

def signup_success(request):
    return render(request, 'success.html')


def login(request):
    if request.method == 'POST':
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to a success page or home
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')

def home_view(request):
    return render(request,'home.html')