from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from services.models import Service
from services.forms import ServiceForm

@login_required
def services(request):
    services = Service.objects.all()
    return render(request, "services/services.html", context={ "services": services })
    
@login_required
@csrf_exempt
def service_create(request):
    form = ServiceForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('services:services')
    return render(request, "services/service_create.html", context={ "form": form })

@login_required
@csrf_exempt
def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    form = ServiceForm(request.POST or None, instance=service)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Sucesso!")
            return redirect(reverse('services:service_update', kwargs={ "pk": pk }))
    return render(request, "services/service_update.html", context={ "form": form, "service": service })

@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, "services/service_delete.html", context={ "service": service })


@login_required
def service_delete_done(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if service:
        service.delete()
        return redirect('services:services')
    return HttpResponse("404")