"""
Book: Building RESTful Python Web Services
Chapter 3: Improving and adding authentication to an API with Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from rest_framework import serializers
from dogsapp.models import Breed
from dogsapp.models import Dog
from django.contrib.auth.models import User
                


class DogSerializer(serializers.HyperlinkedModelSerializer):
    
   
    class Meta:
        model = Dog
        fields = (
            'url',
            'name',
            'age',
            'breedName',
            'color',
            'favoritefood',
            'favoritetoy',
            'gender'
           
            )

class BreedSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Breed
        depth = 4
        fields = (
                'url',
                'breedName',
                'size',
                'exerciseneeds',
                'friendliness',
                'sheddingamount',
                'trainability'
                
                )



