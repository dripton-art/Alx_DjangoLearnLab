from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'publication_year')
	list_filter = ('author', 'publication_year')
	search_fields = ('title', 'author__name')


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Display fields in the user list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')
    
    # Add fields to the form when viewing/editing a user
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    # Add fields to the form when adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)


