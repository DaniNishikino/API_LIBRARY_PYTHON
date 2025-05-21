from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"Author name: {self.name}, Age: {self.age}, Email: {self.email} "

class Book(models.Model):
    name = models.CharField(max_length=155)
    isbn = models.CharField(max_length=13)
    description = models.CharField(max_length=400)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return f"Book name: {self.name}, ISBN: {self.isbn}, Author: {self.author} Book description: {self.description}"

