from django.forms import ModelForm,Form
from web import models
class PaymentForm(ModelForm):
    class Meta:
        model=models.Payment
        fields='__all__'