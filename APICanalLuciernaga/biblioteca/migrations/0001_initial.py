# Generated by Django 2.2.3 on 2019-08-27 15:04

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=225)),
                ('descripcion', models.TextField(max_length=255)),
                ('foto', sorl.thumbnail.fields.ImageField(upload_to='fotos/biblioteca', verbose_name='Imagen')),
                ('archivo', models.FileField(upload_to='documento/biblioteca')),
            ],
            options={
                'verbose_name': 'Biblioteca',
                'verbose_name_plural': 'Biblioteca',
            },
        ),
    ]
