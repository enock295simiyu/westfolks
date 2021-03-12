from django.urls import path
from core import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('languages/', views.Languages.as_view(), name='languages'),
    path('partners/', views.Partners.as_view(), name='partners'),
    path('privacy/', views.Privacy.as_view(), name='privacy'),
    path('support/', views.Support.as_view(), name='support'),

]
