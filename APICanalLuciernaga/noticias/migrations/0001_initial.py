# Generated by Django 2.2.3 on 2019-07-09 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=225)),
                ('descripcion', models.CharField(max_length=225)),
                ('fecha', models.DateField()),
                ('slug', models.SlugField(editable=False, max_length=250, unique=True)),
            ],
        ),
    ]
