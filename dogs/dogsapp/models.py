from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.

class Breed(models.Model):
    
    breedName = models.CharField(max_length=200, unique=True)
    size = models.CharField(max_length=200, unique=False)
    friendliness  = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)], unique=False)
    trainability = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)], unique=False)
    sheddingamount  = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)], unique=False)
    exerciseneeds = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)], unique=False)
    
    def __str__(self):
        return self.breedName
    
class Dog(models.Model):

    name = models.CharField(max_length=200, unique=False)
    age = models.IntegerField()  
    breedName = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=200, unique=False)
    color = models.CharField(max_length=200, unique=False) 
    favoritefood = models.CharField(max_length=200, unique=False) 
    favoritetoy = models.CharField(max_length=200, unique=False) 
    
    def __str__(self):
        return self.name