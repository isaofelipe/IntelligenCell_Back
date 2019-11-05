from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import TesteSerializer, AnaliseSerializer
from .models import Teste, Analise

# Create your views here.
class TesteView(viewsets.ModelViewSet):
    serializer_class = TesteSerializer
    queryset = Teste.objects.all()

class AnaliseView(viewsets.ModelViewSet):
    serializer_class = AnaliseSerializer
    #queryset = Analise.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = AnaliseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('1', status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)