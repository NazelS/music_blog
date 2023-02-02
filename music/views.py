from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.serializers import MusicSerializers
from .models import Music
from .models import Music
# Create your views here.


@api_view(['GET'])
def get_hello(request):#базавая логика         
    # print(dir(request))
    # print(request.user)
    return Response('Hello world')

@api_view(['GET'])# 
def get_music(request, id):
    music= Music.objects.get(id=id)
    serializer = MusicSerializers(music, many=True)
    return Response(serializer.data)
    # print(music)
    # return Response(music)

@api_view(['GET'])# 
def get_song(request, id):
    try:
     soug= Music.objects.get(id=id)
    except Music.DoesNotExist:
     serializer = MusicSerializers(soug, many=False)
    return Response(serializer.data)


@api_view(['POST'])# 
def post_music(request):
    serializer = MusicSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
#serializer переводчик 
# ..../music/1/
# DELETE , PUT, PATCH
# @api_view(['PUT','PATCH'])