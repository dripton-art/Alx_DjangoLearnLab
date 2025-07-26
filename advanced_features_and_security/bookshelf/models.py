from django.db import models
from django.contrib.auth. import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
User = get_user_model()

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	publication_year = models.IntegerField()


	def __str__(self):
		return self.title

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return User

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username