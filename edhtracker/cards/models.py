from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField, JSONField
from django.urls import reverse

from django.conf import settings



class Card(models.Model):
    all_parts = JSONField(null=True)
    arena_id = models.IntegerField(null=True)
    artist = models.CharField(max_length=256)
    booster = models.BooleanField()
    border_color = models.CharField(max_length=256)
    card_faces = JSONField(null=True)
    collector_number = models.CharField(max_length=256)
    colors = ArrayField(models.CharField(max_length=256),null=True)
    color_identity = ArrayField(models.CharField(max_length=256),null=True)
    color_lookup = models.CharField(blank=True,null=True,max_length=256)
    cmc = models.DecimalField(null=True, max_digits=8,decimal_places=1)
    digital = models.BooleanField()
    flavor_text = models.TextField(blank=True,null=True)
    frame = models.CharField(max_length=256)
    frame_effects = ArrayField(models.CharField(max_length=256),null=True)
    foil = models.BooleanField()
    full_art = models.BooleanField()
    games = ArrayField(models.CharField(max_length=256))
    highres_image = models.BooleanField()
    is_commander = models.BooleanField()
    image_uris= models.URLField()
    img_url = models.CharField(default='default.jpg', max_length=256)
    keywords = ArrayField(models.CharField(max_length=256),null=True)
    loyalty = models.CharField(blank=True,null=True,max_length=256)
    layout = models.CharField(max_length=256)
    legalities = JSONField()
    mana_cost = models.CharField(max_length=256,blank=True,null=True)
    mtgo_id = models.IntegerField(null=True)
    multiverse_ids = ArrayField(models.IntegerField(),null=True)
    name = models.CharField(max_length=256)
    nonfoil = models.BooleanField()
    oracle_id = models.CharField(max_length=256)
    oracle_text = models.TextField(blank=True,null=True)
    produced_mana = ArrayField(models.CharField(max_length=256),null=True)
    promo = models.BooleanField()
    promo_types = ArrayField(models.CharField(max_length=256),null=True)
    power = models.CharField(blank=True,null=True,max_length=256)
    oversized = models.BooleanField()
    rarity = models.CharField(max_length=256)
    released_at = models.DateField(null=True)
    related_uris = JSONField(null=True)
    reprint = models.BooleanField()
    reserved = models.BooleanField()
    scryfall_id = models.CharField(default='unkown',max_length=256)
    set = models.CharField(default='unkown',max_length=256)
    set_type = models.CharField(default='unkown',max_length=256)
    set_name = models.CharField(default='unkown',max_length=256)
    story_spotlight = models.BooleanField()
    tcgplayer_id = models.IntegerField(null=True)
    textless = models.BooleanField()
    toughness = models.CharField(blank=True,null=True,max_length=256)
    type_line = models.CharField(blank=True,null=True,max_length=256)
    variation = models.BooleanField()
    variation_of = JSONField(null=True)

    class Meta:
        indexes = [
        models.Index(fields=['set']),
        models.Index(fields=['color_lookup']),
        models.Index(fields=['color_lookup','set'])
    ]

    def __str__(self):
        return self.name

class Commander(models.Model):
    commander = models.ForeignKey(Card, related_name="commander" ,on_delete=models.CASCADE)
    card_list = ArrayField(models.CharField(max_length=256))
    img_url = models.CharField(default='default.jpg', max_length=256)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.commander

class UserCards(models.Model):
    card = models.ForeignKey(Card, related_name="card" ,on_delete=models.CASCADE)
    card_count = models.PositiveIntegerField()
    date_added = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user",on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Set(models.Model):
    arena_code = models.CharField(null=True,max_length=256)
    block = models.CharField(null=True,max_length=256)
    block_code = models.CharField(null=True,max_length=256)
    card_count = models.IntegerField(default=0)
    code = models.CharField(default='unknown',max_length=256)
    digital = models.BooleanField(default=False)
    foil_only = models.BooleanField(default=False)
    img_url = models.CharField(default='default.jpg', max_length=256)
    mtgo_code = models.CharField(null=True,max_length=256)
    name = models.CharField(default='unknown',max_length=256)
    nonfoil_only = models.BooleanField(default=True)
    parent_set_code = models.CharField(null=True,max_length=256)
    released_at = models.DateField(null=True)
    set_type = models.CharField(default='unknown',max_length=256)
    tcgplayer_id = models.IntegerField(null=True)

    class Meta:
        indexes = [
            models.Index(fields=['released_at'])
        ]

    def __str__(self):
        return self.name

