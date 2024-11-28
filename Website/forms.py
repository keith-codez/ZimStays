# forms.py
from django import forms
from .models import Reservation, Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'check_in_date', 'check_in_time', 'check_out_date', 'check_out_time',
            'guests', 'first_name', 'last_name', 'email', 'phone_number', 'additional_info'
        ]
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date' }),
            'check_in_time': forms.TimeInput(attrs={'type': 'time'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_time': forms.TimeInput(attrs={'type': 'time'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Number Of Guests'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name...'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email...'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Phone...'}),
            'additional_info': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Further Information...'}),

        }
        labels = {
            'guests': '', 
            'first_name': '',
            'last_name': '',
            'email':'',
            'phone_number':'',
            'additional_info': '',
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name', 'last_name', 'email', 'phone_number', 'message'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name...'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email...'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Phone...'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Your message...'}),

        }
        labels = { 
            'first_name': '',
            'last_name': '',
            'email':'',
            'phone_number':'',
            'message': '',
        }