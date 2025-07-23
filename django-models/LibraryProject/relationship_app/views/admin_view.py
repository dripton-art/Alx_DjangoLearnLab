from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Helper function to check if user is an Admin
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

# user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_page.html')