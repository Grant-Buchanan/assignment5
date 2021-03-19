from django.db import models

# Create your models here.

class Breed(models.Model):
    
    breedName = models.CharField(max_length=200, unique=True)
    temperment = models.CharField(max_length=200, unique=False)
    lifespan = models.CharField(max_length=2, unique=False)
    
class Dog(models.Model):

    name = models.CharField(max_length=200, unique=False)
    breedName = models.ForeignKey(Breed, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=False)
    age = models.CharField(max_length=200, unique=False)    