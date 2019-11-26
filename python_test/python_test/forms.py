from django.forms import ModelForm
from python_test.models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
