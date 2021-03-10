from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.


from django.utils.decorators import method_decorator
from django.views.generic.base import View

from company.models import Company


@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class CreateCompany(View):
    def get(self, request):
        return render(request, 'company/create/index.html')

    def post(self, request):

        company_name = request.POST['form_fields[first_name]']
        company_url = request.POST['form_fields[last_name]']
        company = Company()
        company.name = company_name
        company.url = company_url
        company.save()
        return redirect('company_create')


@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class CreateCompany(View):
    def get(self, request):
        return render(request, 'company/create/index.html')

    def post(self, request):
        company_name = request.POST['form_fields[first_name]']
        company_url = request.POST['form_fields[last_name]']
        company = Company()
        company.name = company_name
        company.url = company_url
        company.save()
        return redirect('company_create')