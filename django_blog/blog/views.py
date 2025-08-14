from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile


def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # After registration, go to login
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    profile = request.user.userprofile  # automatically created by signals

    if request.method == "POST":
        request.user.username = request.POST.get("username")
        request.user.email = request.POST.get("email")
        request.user.save()

        profile.bio = request.POST.get("bio")
        if request.FILES.get("profile_picture"):
            profile.profile_picture = request.FILES.get("profile_picture")
        profile.save()

        return redirect("profile")

    return render(request, "profile.html", {"profile": profile})
