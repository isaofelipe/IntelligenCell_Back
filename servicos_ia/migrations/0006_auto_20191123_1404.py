# Generated by Django 2.2.5 on 2019-11-23 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos_ia', '0005_auto_20191123_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analise',
            name='imagem_analisada',
            field=models.ImageField(blank=True, null=True, upload_to='imagens_analise/'),
        ),
    ]
