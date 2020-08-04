# Generated by Django 3.0.8 on 2020-07-30 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0013_auto_20200730_1915'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='card',
            name='cards_card_set_ce0598_idx',
        ),
        migrations.AddIndex(
            model_name='card',
            index=models.Index(fields=['set', 'color_lookup', 'id', 'img_url', 'name'], name='cards_card_set_56fdc1_idx'),
        ),
    ]
