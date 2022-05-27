
from django.db import models
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_name(value):
    x = re.match("[a-z]{3}", value,flags=re.IGNORECASE)
    if x==None:
        raise ValidationError(
            _(' Name must have 3 or more letters.'),
            params={'value': value},
        )

class contactFormModel(models.Model):
    firstName = models.CharField("First Name", max_length=50, validators=[validate_name])
    lastName = models.CharField("Last Name", max_length=50, validators=[validate_name])
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.firstName+" "+self.lastName


