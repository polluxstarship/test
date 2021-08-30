from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import *
# Create your views here.

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/admin/')
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else: print(my_form.errors)
#
#     context = {
#         'form': my_form
#     }
#     return render(request, "products/product_create.html", context)


def product_detail_view(request, my_id):
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)

def product_edit_view(request, my_id):   # 데이터베이스에서 불러와 수정하는법
    obj = Product.objects.get(id=my_id)  # 불러오는 조건
    form = ProductForm(request.POST or None, instance=obj) # 객체로 obj를 넣어준다
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_edit.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset,
    }
    return render(request, "products/product_list.html", context)

def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == 'POST':
        print(request.POST)
        obj.delete()
        return redirect("../../")
    context={
        'object': obj
    }
    return render(request, "products/product_delete.html", context)