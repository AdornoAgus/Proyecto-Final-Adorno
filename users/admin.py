from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import user

# Register your models here.

admin.site.register(user, UserAdmin)
