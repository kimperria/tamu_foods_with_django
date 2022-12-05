from django import forms
from .models import DeliverOrder

class DeliverOrderForm(forms.ModelForm):
    class Meta:
        model = DeliverOrder
        fields = '__all__'
        