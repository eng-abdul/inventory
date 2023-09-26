from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
     profile = models.ImageField(upload_to='profile/')
     
     def __str__(self) -> str:
          return self.username

class Customer(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    
    def __str__(self) -> str:
          return self.name
class Categories(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self) -> str:
          return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
          return self.name
    
class ProductOrder(models.Model):
      product = models.ForeignKey(Product, on_delete=models.CASCADE)
      date = models.DateField()
      customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
      
class OrderDetail(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    order = models.ForeignKey(ProductOrder, on_delete=models.CASCADE)
    total = models.CharField(max_length=250)