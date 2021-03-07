from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from accounts.backends import EmailBackend
from accounts.models import Profile


def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)

    except:
        return None
    else:
        if user.check_password(password):
            return user
    return None


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

        email = request.POST['form_fields[email_address]']
        password = request.POST['form_fields[enter_password]']

        user = authenticate_user(email, password)
        context = {}
        print('this is the value of user', user)
        if user is not None:
            login(request, user)
            return redirect(self.request.GET.get('next', 'home'))
        else:
            context['error_message'] = 'Email or Password not correct'
            return render(request, 'account/access/index.html', context)


@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class ProfileUpdate(View):
    def get(self, request):
        return render(request, 'account/update/index.html')

    def post(self, request):
        user = request.user
        first_name = request.POST['form_fields[first_name]']
        last_name = request.POST['form_fields[last_name]']
        current_user = User.objects.get(pk=user.pk)
        email = request.POST['form_fields[email_address]']
        current_user.email = email

        password1 = request.POST['form_fields[update_password]']
        password2 = request.POST['form_fields[confirm_password]']

        current_user.password = password1
        current_user.save()
        profile_headline = request.POST['form_fields[field_91a2f9b]']
        profile_description = request.POST['form_fields[field_86c0ef2]']
        current_employer = request.POST['form_fields[current_employer]']
        current_website = request.POST['form_fields[personal_website]']
        current_city = request.POST['form_fields[current_city]']
        current_state = request.POST['form_fields[current_state]']
        current_country = request.POST['form_fields[field_a98d0c8]']
        professional_services = request.POST['form_fields[professiona_services]']
        professional_specialist = request.POST['form_fields[current_country]']

        profile_image = request.FILES['form_fields[field_3c81bff]']
        fs = FileSystemStorage()
        filename = fs.save(profile_image.name, profile_image)

        profile = Profile.objects.get(user__pk=user.id)
        profile.user = user
        profile.first_name = first_name
        profile.last_name = last_name
        profile.profile_image = profile_image
        profile.profile_headline = profile_headline
        profile.profile_description = profile_description
        profile.current_employer = current_employer
        profile.current_website = current_website
        profile.current_city = current_city
        profile.current_state = current_state
        profile.current_country = current_country
        profile.professional_services = professional_services
        profile.professional_specialist = professional_specialist
        profile.save()
        return redirect('home')
