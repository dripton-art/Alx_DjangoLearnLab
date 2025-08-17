from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

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

   # Comment form and validation
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'}),
        }

    def clean_commnent(self):
        '''custome validation for comment field'''

        content = self.cleaned_data.get('content')

        if len(content) > 2000:
            raise ValidationError('Your comment is too long')