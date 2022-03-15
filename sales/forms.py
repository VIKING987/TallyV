from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from . models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder':'Enter username'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['stockitem', 'rate', 'quantity', 'description']
        widgets = {
            'stockitem': forms.Select(attrs={'class': 'forminput'}),
            'rate': forms.NumberInput(attrs={'class': 'forminput'}),
            'quantity':forms.TextInput(attrs={'class': 'forminput'}),
            'description':forms.Textarea(attrs={'class': 'forminputdescription forminput'}),
        }

class DateInput(forms.DateInput):
    input_type = 'date'

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['party_name', 'date', 'disp_thru', 'bales', 'delivery']
        widgets= {
            'party_name': forms.Select(attrs={'class': 'forminput'}),
            'date': DateInput(attrs={'class': 'forminput'}),
            'disp_thru': forms.TextInput(attrs={'class': 'forminput'}),
            'bales': forms.TextInput(attrs={'class': 'forminput'}),
            'delivery': forms.TextInput(attrs={'class': 'forminput'}),
        }

class PartyCreateForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ['name', 'phone', 'address_line1', 'address_line2', 'payment_recieved']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'forminput'}),
            'phone': forms.TextInput(attrs={'class': 'forminput'}),
            'address_line1':forms.Textarea(attrs={'class': 'forminputaddress forminput'}),
            'address_line2':forms.Textarea(attrs={'class': 'forminputaddress forminput'}),
            'payment_recieved':forms.NumberInput(attrs={'class': 'forminput'})
        }

class StockItemCreateForm(forms.ModelForm):
    class Meta:
        model = StockItem
        fields = ['name', 'per', 'hsncode']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'forminput'}),
            'per': forms.Select(attrs={'class': 'forminput'}),
            'hsncode':forms.TextInput(attrs={'class': 'forminput'}),
        }