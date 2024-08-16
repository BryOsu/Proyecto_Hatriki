from django.db import models
from django.contrib.auth.models import AbstractUser

# Usuario personalizado
class User(AbstractUser):
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set'  # Cambia 'custom_user_set' por lo que desees
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set'  # Cambia 'custom_user_permissions_set' por lo que desees
    )

    def __str__(self):
        return self.username

#Registro de Usuario
class RegisterUser(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name} {self.last_name}"