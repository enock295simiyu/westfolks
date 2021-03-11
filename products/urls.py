from django.urls import path
from products import views

urlpatterns = [
    path('create/', views.CreateProduct.as_view(), name='product_create'),
    path('update/<slug:slug>/',views.UpdateProduct.as_view(),name='product_update'),
    path('product/<slug:slug>/',views.ProductsView.as_view(),name='product'),
    path('',views.Products.as_view(),name='products_page'),
]
