from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.


from django.utils.decorators import method_decorator
from django.views.generic.base import View

from accounts.models import Profile
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
        return redirect('companies_page')



@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class UpdateCompany(View):
    def get(self, request):
        return render(request, 'company/update/index.html')

    def post(self, request):
        company_name = request.POST['form_fields[first_name]']
        company_url = request.POST['form_fields[last_name]']
        company = Company()
        company.name = company_name
        company.url = company_url
        company.save()
        return redirect('companies_page')

@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class CreateCompany(View):
    def get(self, request):
        return render(request, 'company/create/index.html')

    def post(self, request):
        company_name = request.POST['form_fields[first_name]']

        company = Company()
        company.created_by = request.user
        company.name = company_name

        company.save()
        return redirect('companies_page')


@method_decorator(login_required, name='get')
class Companies(View):
    def get(self, request):
        profile = Profile.objects.get(user__pk=request.user.pk)
        companies = Company.objects.filter(created_by=request.user)[:3]
        return render(request, 'company/index.html', {'companies': companies, 'profile': profile})


@method_decorator(login_required, name='get')
class CompanyView(View):
    def get(self, request, slug):
        profile = Profile.objects.get(user__pk=request.user.pk)
        company = Company.objects.get(slug=slug)
        return render(request, 'company/company/index.html', {'company': company})
