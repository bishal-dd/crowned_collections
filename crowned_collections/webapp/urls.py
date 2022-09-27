from django.urls import path
from . import views
from .views import *

app_name = 'webapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('product_page/<slug>/', ProductsDetailView.as_view(), name='product_page'),
    path('order/<slug>/', OrderView.as_view(), name='order'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('searchbar/', searchbar, name='searchbar'),
    path('checkout/', views.checkout, name='checkout')

    ]