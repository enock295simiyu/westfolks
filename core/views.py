from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class HomeView(View):
    def get(self, request):
        return render(request, 'core/index.html')


class About(View):
    def get(self, request):
        return render(request, 'about/index.html')


class Languages(View):
    def get(self, request):
        return render(request, 'languages/index.html')


class Partners(View):
    def get(self, request):
        return render(request, 'partners/index.html')


class Privacy(View):
    def get(self, request):
        return render(request, 'privacy/index.html')


class Support(View):
    def get(self, request):
        return render(request, 'support/index.html')
