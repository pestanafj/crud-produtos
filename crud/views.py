from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

# Create your views here.


# def product_list(request):
#     return render(request, "product_list.html", {"product_list": Product.objects.all()})


# def product_add(request):
#     return render(request, "product_add.html")


class ProductListView(ListView):
    model = Product
    ordering = ["price"]


class ProductCreateView(CreateView):
    model = Product
    fields = ["name_product", "price", "descryption", "available"]
    success_url = reverse_lazy("product_list")
