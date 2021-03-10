from django.urls import path
from company import views

urlpatterns=[
    path('create/',views.CreateCompany.as_view(),name='company_create'),
    path('update/',views.CreateCompany.as_view(),name='company_update'),
]