from django import forms
from .models import Product


class NewOrder(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder':"Full Name", 'class':"form-control"}))
    phone_number = forms.CharField(label='Phone number', required=True, widget=forms.TextInput(attrs={'placeholder':"Phone Number", 'class':"form-control"}))
    address = forms.CharField(label='Address', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder':"Address", 'class':"form-control"}))