# Generated by Django 2.2.3 on 2019-09-10 21:44

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('programacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programacion',
            name='link',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]