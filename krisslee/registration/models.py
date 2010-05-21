from django.db import models

class Registration(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    shirts = models.ManyToMany
    expectation = models.IntegerField()
    
class TShirt(models.Model):
    SIZE_CHOICES = (
        ('XS', 'X-Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'X-Large'),
    )
    number = models.IntegerField()
    size = models.CharField(max_lengt=2, choices=SIZE_CHOICES)
