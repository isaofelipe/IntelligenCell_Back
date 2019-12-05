from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import TesteSerializer, AnaliseSerializer
from .models import Teste, Analise
from uuid import uuid4
from werkzeug.utils import secure_filename
import os
import jsonpickle
from ia_processor.producer import IAProcessorProducer
from rest_framework import generics
from rest_framework.views import APIView
from django.db.models import ImageField
import json
from PIL import ImageFile
from django.core.files import File

# Create your views here.
class TesteView(viewsets.ModelViewSet):
    serializer_class = TesteSerializer
    queryset = Teste.objects.all()

class AnaliseView(viewsets.ModelViewSet):
    serializer_class = AnaliseSerializer
    queryset = Analise.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        analise = Analise.objects.get(id=serializer.data['id'])
        img_analisada = self.call_producer(analise)

        analise.analisada = True
        file_analisada = File(open(img_analisada.name, 'rb'))
        analise.imagem_analisada = file_analisada
        analise.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        img = serializer.validated_data['imagem']
        serializer.save()

    def call_producer(self, analise):
        #image_name = os.path.basename(img['imagem'])
        #image_path = os.path.join('../imagens_analise', image_name)

        #image_path = analise.imagem.name
        image_path = os.path.join('imagens_analise/', analise.imagem.name)

        process_response = jsonpickle.encode({
            'process_id': analise.id,
            'image_path': image_path
        })

        ia_processor_producer = IAProcessorProducer()
        resposta = ia_processor_producer.call(process_response)
        resposta_decodificada = jsonpickle.loads(resposta.decode('utf-8'))
        img_analisada = resposta_decodificada['data']['img_content']
        return img_analisada
