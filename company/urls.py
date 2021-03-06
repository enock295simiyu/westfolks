from django.urls import path
from company import views

urlpatterns = [
    path('', views.Companies.as_view(), name='companies_page'),
    path('create/', views.CreateCompany.as_view(), name='company_create'),
    path('update/<slug:slug>/', views.CreateCompany.as_view(), name='company_update'),
    path('company/<slug:slug>/', views.CompanyView.as_view(), name='company'),
]
