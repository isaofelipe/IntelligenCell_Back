# Generated by Django 2.2.5 on 2019-11-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos_ia', '0004_auto_20191120_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analise',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]