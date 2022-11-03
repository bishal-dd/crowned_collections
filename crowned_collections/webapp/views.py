from .models import Product, Order
from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import NewOrder


def about(request):
    return render(request, 'about.html')


def checkout(request):
    def post():
        return redirect('webapp:home')
    return render(request, 'checkout.html')


def cart(request):
    return render(request, 'cart.html')

def add_to_cart(request, slug):
    product_name = get_object_or_404(Product, slug=slug)
    order_item = Order.objects.create(product_name=str(product_name))
    order_item.save()
    return redirect('webapp:order', slug=slug)


def products(request):
    context = {
        'items': Product.objects.all()
    }
    return render(request, "product_page.html", context)


class HomeView(ListView):
    model = Product
    template_name = "home.html"


class ProductsDetailView(DetailView):
    model = Product
    template_name = "product_page.html"


class OrderView(DetailView):
    def get(self, *args, **kwargs):
        form = NewOrder(self.request.POST or None)
        context = {
            'form': form
        }
        return render(self.request, 'order.html', context)

    def post(self, *args, **kwargs):
        form = NewOrder(self.request.POST or None)
        if form.is_valid():
            order = Order(
                product_name=form.cleaned_data.get('name'),
                FullName=form.cleaned_data.get('name'),
                phone_number=form.cleaned_data.get('phone_number'),
                address=form.cleaned_data.get('address'),
            )
            messages.success(self.request, 'Your order has been placed')
            order.save()
            return redirect('webapp:checkout')
        return redirect('webapp:order')


def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        item = Product.objects.all().filter(product_name=search)
        print(item)
        return render(request, 'searchbar.html', {'item': item})

