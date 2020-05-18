from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


from schedules.models import Schedule
from schedules.forms import ScheduleForm

@login_required
def schedules(request):
    schedules = Schedule.objects.all()
    return render(request, "schedules/schedules.html", context={
        "schedules": schedules
    })

@login_required
@csrf_exempt
def schedule_create(request):
    form = ScheduleForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('schedules:schedules')
    return render(request, "schedules/schedule_create.html", context={ "form": form })

@login_required
@csrf_exempt
def schedule_update(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    form = ScheduleForm(request.POST or None, instance=schedule)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Sucesso!")
            return redirect(reverse('schedules:schedule_update', kwargs={ "pk": pk }))
    return render(request, "schedules/schedule_update.html", context={ "form": form, "schedule": schedule })

@login_required
def schedule_delete(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    return render(request, "schedules/schedule_delete.html", context={ "schedule": schedule })


@login_required
def schedule_delete_done(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if schedule:
        schedule.delete()
        return redirect('schedules:schedules')
    return HttpResponse("404")

def confirm_schedule(request):
    pass

def cancel_schedule(request):
    pass