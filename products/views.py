from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from company.models import Company
from products.models import Product


@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class CreateProduct(View):
    def get(self, request):
        companies = Company.objects.filter(created_by=request.user)

        return render(request, 'product/create/index.html', {'companies': companies})

    def post(self, request):
        product_name = request.POST['form_fields[first_name]']
        product_description = request.POST['form_fields[description]']
        product_url = request.POST['form_fields[url]']
        product_cta = request.POST['form_fields[cta]']
        company_id = request.POST['company']
        company = Company.objects.get(id=company_id)
        product = Product()
        product.name = product_name
        product.description = product_description
        product.cta = product_cta
        product.url = product_url
        product.company = company
        product.save()
        return redirect('product_create')
