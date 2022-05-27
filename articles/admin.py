from django.contrib import admin

from articles.models import article,Author

admin.site.register(article)
admin.site.register(Author)