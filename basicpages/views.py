from django.shortcuts import render

from articles.models import article
from .forms import contactForm
from django.contrib import messages
from .models import contactFormModel
from django.views.generic import TemplateView,ListView


class home_view(ListView):
    model = article
    queryset = article.objects.order_by('-id')[:4]
    template_name = "basicpages/index.html"
    
class about_view(TemplateView):
    template_name = "basicpages/about.html"

def contact_view(request):
    form = contactForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Message sent, thanks for getting intouch with us.')
    return render(request, 'basicpages/contact.html',{'form':form})

