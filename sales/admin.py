from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Users)
admin.site.register(Categories)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(OrderDetail)
