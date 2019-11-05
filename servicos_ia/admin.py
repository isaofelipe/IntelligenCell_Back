from django.contrib import admin

# Register your models here.
from .models import Teste
from .models import Analise

class TesteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'ativo')

class AnaliseAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'imagem', 'resultado')

admin.site.register(Teste, TesteAdmin)
admin.site.register(Analise, AnaliseAdmin)