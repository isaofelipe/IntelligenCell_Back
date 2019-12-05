from django.db import models

class Teste(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    ativo = models.BooleanField(default=False)

    def _str_(self):
        return self.nome

class Analise(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=10)
    imagem = models.ImageField(upload_to='')
    imagem_analisada = models.ImageField(upload_to='', blank=True, null=True)
    analisada = models.BooleanField(default=False)

    def _str_(self):
        return self.modelo + '_analisada: ' + self.analisada

class Objeto_analise(models.Model):
    analise = models.ForeignKey(Analise, on_delete=models.CASCADE)
    label = models.CharField(max_length=20)