from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.AccountView.as_view(),name='account-view'),
    path('access/', views.Login.as_view(), name='login'),
    path('update/', views.ProfileUpdate.as_view(), name='profile-update'),
    path('reset/', views.AccountReset.as_view(), name='reset-password'),
    path('create/', views.AccountCreateForm.as_view(), name='signup'),
    path('page/', views.AccountPage.as_view(), name='account_page'),
    path('crawl/', views.Crawl.as_view(), name='company_crawl'),

]