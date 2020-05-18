import json

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from products.models import Product
from products.forms import ProductForm, ProductExitEntryForm

@login_required
def products(request):
    products = Product.objects.all()
    form = ProductExitEntryForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('products:products')
    return render(request, "products/products.html", context={
        "products": products,
        "form": form,
    })

@login_required
@csrf_exempt
def product_create(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('products:products')
    return render(request, "products/product_create.html", context={ "form": form })

@login_required
@csrf_exempt
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Sucesso!")
            return redirect(reverse('products:product_update', kwargs={ "pk": pk }))
    return render(request, "products/product_update.html", context={ "form": form, "product": product })

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_delete.html", context={ "product": product })


@login_required
def product_delete_done(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product:
        product.delete()
        return redirect('products:products')
    return HttpResponse("404")

@login_required
@csrf_exempt
def change_stock(request):
    if request.method == "POST":
        data = json.loads(request.body)

        pk = data.get('pk')
        stock_exit = data.get('stock_exit') or None
        stock_entry = data.get('stock_entry') or None

        product = Product.objects.get(pk=pk)
        if product:
            if stock_exit:
                product.stock_exit = int(data.get('stock_exit'))
            if stock_entry:
                product.stock_entry = int(data.get('stock_entry'))
            product.save()
            product.get_current_quantity()
            
            return JsonResponse({ "status": 200 })
        else:
            return JsonResponse({ "status": 500 })