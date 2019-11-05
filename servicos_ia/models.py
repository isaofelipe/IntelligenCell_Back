from django.db import models

class Teste(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    ativo = models.BooleanField(default=False)

    def _str_(self):
        return self.nome

class Analise(models.Model):
    modelo = models.CharField(max_length=10)
    imagem = models.ImageField(upload_to = 'imagens_analise/')
    resultado = models.CharField(max_length=3, blank=True)

    def _str_(self):
        return self.modelo + '_' + self.resultado