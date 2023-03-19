from django.forms import ModelForm

from .models import BooksModel


class BookForm(ModelForm):
    class Meta:
        model = BooksModel
        fields = ['title', 'author', 'publisher']