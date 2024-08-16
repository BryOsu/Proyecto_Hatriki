from django.db import models
from App_user.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='img/kits/')
    field_name = models.URLField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.product.name}'