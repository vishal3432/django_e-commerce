from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    # Tags ka use hum AI model mein similarity score nikalne ke liye karenge
    tags = models.CharField(max_length=255, help_text="Comma separated tags (e.g. tech, mobile, fast)")

    def __str__(self):
        return self.name

class Interaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Like = 1, Dislike = -1, View = 0
    score = models.IntegerField(default=0) 
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"