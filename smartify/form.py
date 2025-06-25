from .models import User
from django import forms

class UseR(forms.ModelForm):

    class Meta:
        model = User
        fields = ['full_name', 'phone_number']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'WhatsApp Phone Number'}),
        }