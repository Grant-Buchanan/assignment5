from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from dogsapp.models import Breed as breed_model
from dogsapp.models import Dog as dogs_model
from dogsapp.serializers import DogSerializer
from dogsapp.serializers import BreedSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
class DogsList(generics.ListCreateAPIView):
    queryset = dogs_model.objects.all()
    serializer_class = DogSerializer
    name = 'dog-list'   
 
        
class DogsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = dogs_model.objects.all()
    serializer_class = DogSerializer
    name = 'dog-detail'     
  
        
class BreedsList(generics.ListCreateAPIView):
    queryset = breed_model.objects.all()
    serializer_class = BreedSerializer
    name = 'breed-list'
    
      
class BreedsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = breed_model.objects.all()
    serializer_class = BreedSerializer
    name = 'breed-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'dogs': reverse(PlayerList.name, request=request),
            'dog-breeds': reverse(GameCategoryList.name, request=request),
        
            })