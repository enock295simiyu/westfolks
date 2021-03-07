from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

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
