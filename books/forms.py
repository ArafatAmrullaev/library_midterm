from django.forms import ModelForm

from .models import BooksModel, AuthorModel, PublisherModel


class BookForm(ModelForm):
    class Meta:
        model = BooksModel
        fields = ['title', 'author', 'publisher', 'cover']


class AuthorForm(ModelForm):
    class Meta:
        model = AuthorModel
        fields = ['name', 'email',]

    
class PublisherForm(ModelForm):
    class Meta:
        model = PublisherModel
        fields = ['name', 'address']