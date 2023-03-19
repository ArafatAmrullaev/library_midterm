from django.db import models

# Create your models here.

class BooksModel(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('AuthorModel', on_delete=models.CASCADE)
    publisher = models.ForeignKey('PublisherModel', on_delete=models.CASCADE)
    public_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class AuthorModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name


class PublisherModel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name



