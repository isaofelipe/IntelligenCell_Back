from rest_framework import serializers
from .models import Teste
from .models import Analise

class TesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teste
        fields = ('nome', 'descricao', 'ativo')

class AnaliseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analise
        fields = ('id', 'modelo', 'imagem', 'imagem_analisada', 'analisada')
