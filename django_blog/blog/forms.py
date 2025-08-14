from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # new field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # include email here

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # save email too
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']