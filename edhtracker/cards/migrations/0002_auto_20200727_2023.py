# Generated by Django 3.0.8 on 2020-07-28 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='set',
            index=models.Index(fields=['released_at'], name='cards_set_release_ddd8cd_idx'),
        ),
    ]
