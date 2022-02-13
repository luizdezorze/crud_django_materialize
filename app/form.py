from django.forms import ModelForm
from app.models import Tratamentos


# Create the form class.
class TratamentosForm(ModelForm):
    class Meta:
        model = Tratamentos
        fields = '__all__'