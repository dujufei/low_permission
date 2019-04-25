from django.forms import ModelForm,Form
from web import models

class CustomerForm(ModelForm):
    class Meta:
        model=models.Customer
        fields='__all__'