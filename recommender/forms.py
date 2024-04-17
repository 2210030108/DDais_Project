from django import forms

class WashingMachineFilterForm(forms.Form):
    PRICE_CHOICES = [
        ('0', 'Any Price'),
        ('10000', 'Up to ₹10,000'),
        ('20000', '₹10,000 - ₹20,000'),
        ('30000', '₹20,000 - ₹30,000'),
        ('32000', '₹30,000 and above')
    ]

    price_range = forms.ChoiceField(choices=PRICE_CHOICES, label='Price Range')
