from django.contrib import admin

from .models import BooksModel, AuthorModel, PublisherModel

# Register your models here.

admin.site.register(BooksModel)
admin.site.register(AuthorModel)
admin.site.register(PublisherModel)