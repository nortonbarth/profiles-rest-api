from django.contrib import admin
from profiles_api import models
# Register your models here.

class UserProfile_adminClass(admin.ModelAdmin):
    list_display = ("email", "is_staff", "is_superuser")

admin.site.register(models.UserProfile,UserProfile_adminClass)