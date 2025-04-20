from django import forms
from .models import Orders

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

        labels = {
            'oid': 'Order ID',
            'fname' : 'First Name',
            'lname' : 'Last Name.' ,
            'price' : 'Price' ,
            'mail' : 'Email ID',
            'addr' : 'Address' ,
        }

        widgets  ={
            'oid' : forms.NumberInput(attrs={'placeholder': '1'}),
            'fname' : forms.TextInput(attrs={'placeholder': 'Thoti'}),
            'lname' : forms.TextInput(attrs={'placeholder': 'Rajesh'}),
            'price' : forms.NumberInput(attrs={'placeholder': '30000'}),
            'mail' : forms.EmailInput(attrs={'placeholder': 'rajesh@example.com'}),
            'addr' : forms.Textarea(attrs={'placeholder': 'Tirupati'}),
        }