from django.contrib import admin
from .models import User, RegisterUser

admin.site.register(User)
admin.site.register(RegisterUser)