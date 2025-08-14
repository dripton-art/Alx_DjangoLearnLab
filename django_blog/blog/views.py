from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # After registration, go to login
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

