from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Helper function to check if user is a Member
def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'
    
def member_view(request):
    return render(request, 'relationship_app/member_page.html')