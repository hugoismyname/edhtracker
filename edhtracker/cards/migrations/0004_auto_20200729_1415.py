# Generated by Django 3.0.8 on 2020-07-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20200728_1344'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='card',
            index=models.Index(fields=['color_lookup'], name='cards_card_color_l_41c95c_idx'),
        ),
    ]
