from django.db import models

# Create your models here.
class lab(models.Model):
    book_name=models.CharField(max_length=200)
    author=models.CharField(max_length=120)
    isbn=models.CharField(max_length=15)
    quantity=models.IntegerField()
    category=models.CharField(max_length=120)
