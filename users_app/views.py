from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserForm
from django.contrib.auth import authenticate, login

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('home'))
    else:
        form = UserForm()
    return render(request, 'users_app/signup.html', {'form': form})