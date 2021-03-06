# Generated by Django 3.0.8 on 2020-07-22 18:44

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_parts', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('arena_id', models.IntegerField(null=True)),
                ('artist', models.CharField(max_length=256)),
                ('booster', models.BooleanField()),
                ('border_color', models.CharField(max_length=256)),
                ('card_faces', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('collector_number', models.CharField(max_length=256)),
                ('colors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), null=True, size=None)),
                ('color_identity', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), null=True, size=None)),
                ('color_lookup', models.CharField(blank=True, max_length=256, null=True)),
                ('cmc', models.DecimalField(decimal_places=1, max_digits=8, null=True)),
                ('digital', models.BooleanField()),
                ('flavor_text', models.TextField(blank=True, null=True)),
                ('frame', models.CharField(max_length=256)),
                ('frame_effects', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), null=True, size=None)),
                ('foil', models.BooleanField()),
                ('full_art', models.BooleanField()),
                ('games', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=None)),
                ('highres_image', models.BooleanField()),
                ('is_commander', models.BooleanField()),
                ('image_uris', models.URLField()),
                ('img_url', models.CharField(default='default.jpg', max_length=256)),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), null=True, size=None)),
                ('loyalty', models.CharField(blank=True, max_length=256, null=True)),
                ('layout', models.CharField(max_length=256)),
                ('legalities', django.contrib.postgres.fields.jsonb.JSONField()),
                ('mana_cost', models.CharField(blank=True, max_length=256, null=True)),
                ('mtgo_id', models.IntegerField(null=True)),
                ('multiverse_ids', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None)),
                ('name', models.CharField(max_length=256)),
                ('nonfoil', models.BooleanField()),
                ('oracle_id', models.CharField(max_length=256)),
                ('oracle_text', models.TextField(blank=True, null=True)),
                ('produced_mana', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), null=True, size=None)),
                ('promo', models.BooleanField()),
                ('promo_types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), null=True, size=None)),
                ('power', models.CharField(blank=True, max_length=256, null=True)),
                ('oversized', models.BooleanField()),
                ('rarity', models.CharField(max_length=256)),
                ('released_at', models.DateField(null=True)),
                ('related_uris', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('reprint', models.BooleanField()),
                ('reserved', models.BooleanField()),
                ('scryfall_id', models.CharField(default='unkown', max_length=256)),
                ('set', models.CharField(default='unkown', max_length=256)),
                ('set_type', models.CharField(default='unkown', max_length=256)),
                ('set_name', models.CharField(default='unkown', max_length=256)),
                ('story_spotlight', models.BooleanField()),
                ('tcgplayer_id', models.IntegerField(null=True)),
                ('textless', models.BooleanField()),
                ('toughness', models.CharField(blank=True, max_length=256, null=True)),
                ('type_line', models.CharField(blank=True, max_length=256, null=True)),
                ('variation', models.BooleanField()),
                ('variation_of', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arena_code', models.CharField(max_length=256, null=True)),
                ('block', models.CharField(max_length=256, null=True)),
                ('block_code', models.CharField(max_length=256, null=True)),
                ('card_count', models.IntegerField(default=0)),
                ('code', models.CharField(default='unknown', max_length=256)),
                ('digital', models.BooleanField(default=False)),
                ('foil_only', models.BooleanField(default=False)),
                ('img_url', models.CharField(default='default.jpg', max_length=256)),
                ('mtgo_code', models.CharField(max_length=256, null=True)),
                ('name', models.CharField(default='unknown', max_length=256)),
                ('nonfoil_only', models.BooleanField(default=True)),
                ('parent_set_code', models.CharField(max_length=256, null=True)),
                ('released_at', models.DateField(null=True)),
                ('set_type', models.CharField(default='unknown', max_length=256)),
                ('tcgplayer_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_count', models.PositiveIntegerField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('img_url', models.CharField(default='default.jpg', max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card', to='cards.Card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commander',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_list', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=None)),
                ('img_url', models.CharField(default='default.jpg', max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('commander', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commander', to='cards.Card')),
            ],
        ),
    ]
