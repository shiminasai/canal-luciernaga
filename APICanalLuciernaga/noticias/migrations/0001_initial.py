# Generated by Django 2.2.3 on 2019-07-12 21:40

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lugar', '0001_initial'),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=225)),
                ('categoria', models.ManyToManyField(to='noticias.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Comunicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=225)),
                ('autor', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('foto', models.ImageField(upload_to='fotos/noticias')),
                ('descripcion', models.CharField(max_length=225)),
                ('fuente', models.CharField(max_length=225)),
                ('ultimo_momento', models.BooleanField()),
                ('slug', models.SlugField(editable=False, max_length=250, unique=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticias.Categoria')),
                ('clasificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticias.Clasificacion')),
                ('pais', models.ForeignKey(on_delete=255, to='lugar.Pais')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('tipo', models.ForeignKey(on_delete=225, to='noticias.Tipo')),
            ],
        ),
    ]
