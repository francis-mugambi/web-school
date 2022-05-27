from email import header
from xml.dom.minidom import Attr
from django.db import models
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_name(value):
    x = re.match("[a-z-]{5}", value,flags=re.IGNORECASE)
    if x==None:
        raise ValidationError(
            _(' White spaces are not allowed! use (-) between words'),
            params={'value': value},
        )


class article(models.Model):
    BLOG_CATEGORY = (
        ('TEC', 'Technical'),
        ('PRO', 'Programming'),
        ('HOW', 'HOW TO'),
        ('OTH', 'Other')
    )
    blog_category = models.CharField(max_length=3, choices=BLOG_CATEGORY)
    title = models.CharField("Page Title", max_length=150)
    url_name = models.CharField("Url Name", max_length=40, validators=[validate_name])
    photo = models.ImageField(upload_to='photos')
    paragrah1 = models.TextField("Paragraph1")
    header2 = models.CharField("Header2 (optional)", max_length=150)
    paragrah2 = models.TextField("Paragraph2")
    header3 = models.CharField("Header3 (optional)", max_length=150)
    paragrah3 = models.TextField("Paragraph3")
    header4 = models.CharField("Header4 (optional)", max_length=150)
    paragrah4 = models.TextField("Paragraph4")
    header5 = models.CharField("Header5 (optional)", max_length=150)
    paragrah5 = models.TextField("Paragraph5")
    release_date = models.DateField()

    def __str__(self):
        return self.title


from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=200,  help_text="Please use the following format: <em>YYYY-MM-DD</em>."
)
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})

    class Meta:
       verbose_name= 'name'
