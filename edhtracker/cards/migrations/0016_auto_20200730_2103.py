# Generated by Django 3.0.8 on 2020-07-31 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0015_auto_20200730_1943'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='card',
            name='cards_card_set_513cb1_idx',
        ),
        migrations.AddIndex(
            model_name='card',
            index=models.Index(condition=models.Q(is_variation=False), fields=['set', 'color_lookup', 'name', 'id', 'img_url'], name='cards_by_set'),
        ),
    ]
