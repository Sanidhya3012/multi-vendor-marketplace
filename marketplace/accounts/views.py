from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('/')  # or redirect to profile/dashboard
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})