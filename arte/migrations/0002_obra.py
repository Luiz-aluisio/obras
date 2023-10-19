# Generated by Django 4.2.6 on 2023-10-19 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arte', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('descricao', models.CharField(max_length=240)),
                ('data_de_publicacao', models.DateField(null=True)),
                ('data_de_exposicao', models.DateField(null=True)),
                ('autores', models.ManyToManyField(to='arte.autor')),
            ],
        ),
    ]
