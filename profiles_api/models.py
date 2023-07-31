from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

    
class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, password=None):

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email),name=name)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, name, password):
        """Create and save new superUser profile"""

        
        user =self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255,unique=True,blank=False)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrive the full name"""
        return self.name
    
    def get_short_name(self):
        """Retrive the short name"""
        return self.name
    
    def __str__(self) -> str:
        return f'{self.email} '