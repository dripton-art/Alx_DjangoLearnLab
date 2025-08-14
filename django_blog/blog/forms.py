from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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