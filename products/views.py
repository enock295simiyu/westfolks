from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from accounts.models import Profile
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
        return redirect('products_page')


@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class UpdateProduct(View):
    def get(self, request, slug):
        companies = Company.objects.filter(created_by=request.user)
        product=Product.objects.get(slug=slug)

        return render(request, 'product/update/index.html', {'companies': companies,'product':product})

    def post(self, request, slug):
        product_description = request.POST['form_fields[description]']
        product_url = request.POST['form_fields[url]']
        product_cta = request.POST['form_fields[cta]']
        company_id = request.POST['company']
        company = Company.objects.get(id=company_id)
        product = Product.objects.get(slug=slug)
        product.description = product_description
        product.cta = product_cta
        product.url = product_url
        product.company = company
        product.save()
        return redirect('products_page')


@method_decorator(login_required, name='get')
class Products(View):
    def get(self, request):
        profile = Profile.objects.get(user__pk=request.user.pk)
        products = Product.objects.filter(company__created_by=request.user)[:3]
        return render(request, 'product/index.html', {'products': products, 'profile': profile})


@method_decorator(login_required, name='get')
class ProductsView(View):
    def get(self, request, slug):
        profile = Profile.objects.get(user__pk=request.user.pk)
        product = Product.objects.get(slug=slug)
        return render(request, 'product/product/index.html', {'product': product})
