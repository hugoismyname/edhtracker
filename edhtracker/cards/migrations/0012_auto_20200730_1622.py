# Generated by Django 3.0.8 on 2020-07-30 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0011_auto_20200730_1609'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='card',
            name='cards_card_color_l_41c95c_idx',
        ),
        migrations.RemoveIndex(
            model_name='card',
            name='cards_card_set_ce0598_idx',
        ),
        migrations.AddIndex(
            model_name='card',
            index=models.Index(fields=['set'], name='cards_card_set_b54906_idx'),
        ),
    ]
