from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from pets.models import Pets
from pets.forms import PetForm

@login_required
def pets(request):
    pets = Pets.objects.all()
    return render(request, "pets/pets.html", context={ "pets": pets })

@login_required
@csrf_exempt
def pet_create(request):
    pet_create = PetForm(request.POST or None)
    if request.method == "POST":
        if pet_create.is_valid():
            pet_create.save()
            return redirect('pets:pets')
    return render(request, "pets/pet_create.html", context={ "pet_create": pet_create })

@login_required
@csrf_exempt
def pet_update(request, pk):
    pet = get_object_or_404(Pets, pk=pk)
    pet_update = PetForm(request.POST or None, instance=pet)
    if request.method == "POST":
        if pet_update.is_valid():
            pet_update.save()
            messages.success(request, "Sucesso!")
            return redirect('pets:pets')
    return render(request, "pets/pet_update.html", context={ "pet_update": pet_update, "pet": pet })

@login_required
def pet_delete(request, pk):
    pet = get_object_or_404(Pets, pk=pk)
    return render(request, "pets/pet_delete.html", context={ "pet": pet })

@login_required
def pet_delete_done(request, pk):
    pet = get_object_or_404(Pets, pk=pk)
    if pet:
        pet.delete()
        return redirect('pets:pets')
    return HttpResponse("404")
