from django.urls import path
from products import views

urlpatterns = [
    path('create/', views.CreateProduct.as_view(), name='product_create')
]
