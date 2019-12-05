# Generated by Django 2.2.5 on 2019-11-20 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicos_ia', '0003_auto_20191105_0101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analise',
            name='resultado',
        ),
        migrations.AddField(
            model_name='analise',
            name='analisada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='analise',
            name='imagem_analisada',
            field=models.ImageField(null=True, upload_to='imagens_analise/'),
        ),
        migrations.CreateModel(
            name='Objeto_analise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=20)),
                ('analise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos_ia.Analise')),
            ],
        ),
    ]
