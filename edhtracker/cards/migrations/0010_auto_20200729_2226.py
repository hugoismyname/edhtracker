# Generated by Django 3.0.8 on 2020-07-30 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0009_auto_20200729_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='variation',
            new_name='is_variation',
        ),
        migrations.RemoveField(
            model_name='card',
            name='variation_of',
        ),
    ]