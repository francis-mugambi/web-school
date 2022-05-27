from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='HTMLapp/html_home_page.html'), name='home-page'),
    path('html-structure/', TemplateView.as_view(template_name='HTMLapp/html_structure.html')),
    path('html-headings/', TemplateView.as_view(template_name='HTMLapp/html_headings.html')),   
    path('html-sematics/', TemplateView.as_view(template_name='HTMLapp/html_sematics.html')),
    path('html-comments/', TemplateView.as_view(template_name='HTMLapp/html_comments.html')),
    path('html-styles/', TemplateView.as_view(template_name='HTMLapp/html_styles.html')),
    path('html-formatting/', TemplateView.as_view(template_name='HTMLapp/html_formatting.html')),
    path('html-css/', TemplateView.as_view(template_name='HTMLapp/html_css.html')),
    path('html-colors/', TemplateView.as_view(template_name='HTMLapp/html_colors.html')),
    path('html-lists/', TemplateView.as_view(template_name='HTMLapp/html_lists.html')),
    path('html-images/', TemplateView.as_view(template_name='HTMLapp/html_images.html')),
    path('html-tables/', TemplateView.as_view(template_name='HTMLapp/html_tables.html')),
    path('html-class/', TemplateView.as_view(template_name='HTMLapp/html_class.html')),
    path('html-id/', TemplateView.as_view(template_name='HTMLapp/html_id.html')),
    path('html-meta-data/', TemplateView.as_view(template_name='HTMLapp/html_meta_data.html')),
    path('html-symbols/', TemplateView.as_view(template_name='HTMLapp/html_symbols.html')),
    path('html-iframes/', TemplateView.as_view(template_name='HTMLapp/html_iframes.html')),
    path('html-javascript/', TemplateView.as_view(template_name='HTMLapp/html_javascript.html')),
    path('html-forms/', TemplateView.as_view(template_name='HTMLapp/html_forms.html')),
    path('html-form-elements/', TemplateView.as_view(template_name='HTMLapp/html_form_elements.html')),
    path('html-input-types/', TemplateView.as_view(template_name='HTMLapp/html_input_types.html')),
    path('html-input-attributes/', TemplateView.as_view(template_name='HTMLapp/html_input_attributes.html')),
    path('html-audio/', TemplateView.as_view(template_name='HTMLapp/html_audio.html')),
    path('html-video/', TemplateView.as_view(template_name='HTMLapp/html_video.html')),
    path('html-youtube/', TemplateView.as_view(template_name='HTMLapp/html_youtube.html')),
    path('html-canvas/', TemplateView.as_view(template_name='HTMLapp/html_canvas.html')),
    path('html-svg/', TemplateView.as_view(template_name='HTMLapp/html_svg.html')),
    path('html-plugins/', TemplateView.as_view(template_name='HTMLapp/html_plugins.html')),
   
]