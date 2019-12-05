# Configurações do retina-net

Navegar até a pasta do retina pelo terminal

- Passo 1 - Digitar: pip install numpy --user
- Passo 2 - Digitar: pip install . --user
- Passo 3 - Digitar: python setup.py build_ext --inplace
- Passo 4 - Cria uma pasta chamada "models" e dentro dela criar outra chamada "inference"
- Passo 5 - Adicionar o 'cells.h5' na pasta models/inference

# Configurações do IA Processore

- Passo 1 - Certificar que exista uma pasta chamada "uploads"
- Passo 2 - Rodar o arquivo webserver.py e consumer.py

# Outros passos

# instalar e rodar rabbitmq
- (https://www.youtube.com/watch?v=eazz-Je4HAA)
- http://localhost:15672

#Alterações no models
- python manage.py makemigrations servicos_ia
- python manage.py migrate servicos_ia
- python manage.py flush (limpar base de dados)

#Criar superuser
- python manage.py createsuperuser

#Anotações
- Adicionar campo nome na Analise para identificação