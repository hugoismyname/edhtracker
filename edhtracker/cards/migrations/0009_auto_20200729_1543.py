# Generated by Django 3.0.8 on 2020-07-29 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_auto_20200729_1540'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='card',
            index=models.Index(fields=['color_lookup', 'set'], name='cards_card_color_l_666799_idx'),
        ),
    ]
