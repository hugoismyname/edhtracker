# Generated by Django 3.0.8 on 2020-08-04 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0023_auto_20200803_1418'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='commander',
            index=models.Index(fields=['name'], name='commander_rec'),
        ),
    ]