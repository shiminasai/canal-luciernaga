# Generated by Django 2.2.3 on 2019-08-12 19:29

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('videoteca', '0005_remove_episodio_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodio',
            name='imagen',
            field=sorl.thumbnail.fields.ImageField(default=1, upload_to='fotos/videos', verbose_name='Imagen'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='imagen',
            field=sorl.thumbnail.fields.ImageField(default=1, upload_to='fotos/videos', verbose_name='Imagen'),
            preserve_default=False,
        ),
    ]
