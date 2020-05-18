from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from accounts.models import User
from pets.models import Pets

from core.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
    
@login_required
def index(request):

    clients = User.objects.filter(user_type="C").exclude(is_superuser=True)
    employees = User.objects.filter(user_type="F").exclude(is_superuser=True)
    pets = Pets.objects.all()

    return render(request, "index.html", context={
        "clients": clients,
        "employees": employees,
        "pets": pets
    })

def reset(request):
    if request.method == "POST":

        email = request.POST.get('user_email')
        user = User.objects.get(email=email)
        if user:

            current_site = get_current_site(request).domain
            subject = "Redefinição de senha enviada!"
            token = account_activation_token.make_token(user)
            reset_confirm_reverse = reverse('reset_confirm', kwargs={ "token": token, "pk": user.pk })
            url = "{}{}".format(current_site, reset_confirm_reverse)

            message = url

            send_mail(subject, message, 'petshopclienteteste@gmail.com', [email], fail_silently=False)
            return redirect('reset_done')

    return render(request, "registration/reset.html", context={})

def reset_done(request):
    return render(request, "registration/reset_done.html", context={})

def reset_confirm(request, pk, token):

    user = User.objects.get(pk=pk)

    if request.method == "POST":

        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if (password1 and password2) and (password1 == password2):

            user.set_password(password1)
            user.save()
            return redirect('reset_complete')
            
        else:
            pass

    return render(request, "registration/reset_confirm.html", context={ })

def reset_complete(request):
    return render(request, "registration/reset_complete.html", context={

    })
