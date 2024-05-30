from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfull login')
            return redirect('home:home')
    
    context = { "form": form }
    return render(request, "login.html", context)


def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        new_user = User(username=username, password=password)
        new_user.save()

        login(request, new_user)
        messages.success(request, 'Successfull login')  

        return redirect('home:home')
    

    context = { 'form': form }
    return render(request, 'register.html', context)



def logout_view(request):
    logout(request)
    return redirect("home:home")