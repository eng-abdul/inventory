from django.urls import path
from . import views
urlpatterns = [
    path('', views.signin),
    path('logout', views.signout,name='logout'),
    path('login', views.signin, name='login'),
    path('home', views.home, name='home'),
    path('customer', views.customer, name='customer'),
    path('product', views.product, name='product'),
    path('order', views.prduct_order,name='order'),
    path('category', views.category, name='category')
]
