from .models import contactFormModel
from django.forms import ModelForm

class contactForm(ModelForm):
    class Meta:
        model = contactFormModel
        fields = '__all__'
