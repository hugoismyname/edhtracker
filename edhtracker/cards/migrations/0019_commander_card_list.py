# Generated by Django 3.0.8 on 2020-07-31 19:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0018_remove_commander_card_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='commander',
            name='card_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[0], size=None),
            preserve_default=False,
        ),
    ]
