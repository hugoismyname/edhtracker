# Generated by Django 3.0.8 on 2020-07-30 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0010_auto_20200729_2226'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='card',
            name='cards_card_set_b54906_idx',
        ),
        migrations.RemoveIndex(
            model_name='card',
            name='cards_card_color_l_666799_idx',
        ),
        migrations.AddIndex(
            model_name='card',
            index=models.Index(fields=['set', 'color_lookup'], name='cards_card_set_ce0598_idx'),
        ),
    ]