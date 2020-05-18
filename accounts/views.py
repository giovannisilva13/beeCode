
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from accounts.models import User
from accounts.forms import UserForm, EmployeeForm

@login_required
def clients(request):
    clients = User.objects.filter(user_type="C").exclude(is_superuser=True)
    return render(request, "clients/clients.html", context={ "clients": clients })

@login_required
@csrf_exempt
def client_create(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('accounts:clients')
    return render(request, "clients/client_create.html", context={ "form": form })

@login_required
@csrf_exempt
def client_update(request, pk):
    client = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=client)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Sucesso!")
            return redirect('accounts:clients')
    return render(request, "clients/client_update.html", context={ "form": form, "client": client })

@login_required
def client_delete(request, pk):
    client = get_object_or_404(User, pk=pk)
    return render(request, "clients/client_delete.html", context={ "client": client })

@login_required
def client_delete_done(request, pk):
    client = get_object_or_404(User, pk=pk)
    if client:
        client.delete()
        return redirect('accounts:clients')
    return HttpResponse("404")


@login_required
def employees(request):
    employees = User.objects.filter(user_type="F").exclude(is_superuser=True)
    return render(request, "employees/employees.html", context={ "employees": employees })
    
@login_required
@csrf_exempt
def employee_create(request):
    form = EmployeeForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('accounts:employees')
    return render(request, "employees/employee_create.html", context={ "form": form })

@login_required
@csrf_exempt
def employee_update(request, pk):
    try:
        employee = get_object_or_404(User, pk=pk)
        form = EmployeeForm(request.POST or None, instance=employee)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Sucesso!")
                return redirect('accounts:employees')
        return render(request, "employees/employee_update.html", context={ "form": form, "employee": employee })
    except:
        return HttpResponse("404")

@login_required
def employee_delete(request, pk):
    try:
        employee = get_object_or_404(User, pk=pk)
        return render(request, "employees/employee_delete.html", context={ "employee": employee })
    except:
        return HttpResponse("404")

@login_required
def employee_delete_done(request, pk):
    try:
        employee = get_object_or_404(User, pk=pk)
        employee.delete()
        return redirect('accounts:employees')
    except:
        return HttpResponse("404")

@login_required
@csrf_exempt
def change_password(request):
    form = PasswordChangeForm(request.user, request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:change_password')
    return render(request, 'change_password.html', { 'form': form })