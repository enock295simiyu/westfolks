from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from accounts.backends import EmailBackend
from accounts.forms import SignUpForm


class AccountCreateForm(View):
    def get(self, request):
        return render(request, 'account/create/index.html')

    def post(self, request):
        user = User()
        user.first_name = request.POST['form_fields[first_name]']
        user.last_name = request.POST['form_fields[last_name]']
        user.email = request.POST['form_fields[email_address]']
        user.password = request.POST['form_fields[create_password]']
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'account/access/index.html')

    def post(self, request):
        print(request.POST)
        email = request.POST['form_fields[email_address]']
        password = request.POST['form_fields[enter_password]']
        email_backend=EmailBackend()
        user =  email_backend.authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/access/index.html')
