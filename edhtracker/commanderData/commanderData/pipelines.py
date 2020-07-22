# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from MTG_cards.models import Commander
from MTG_cards.models import Card

class CommanderdataPipeline(object):
    def process_item(self, item, spider):
        commander_query = Card.objects.filter(name__icontains=item['commander']).filter(is_commander=True)
        is_showcase = commander_query.filter(frame_effects__icontains='showcase')
        is_borderless = commander_query.filter(border_color__contains='borderless')

        if is_showcase:
            card = is_showcase.first()
            print(1)
        elif is_borderless:
            print(2)
            card = is_borderless.first()
        else:
            print(3)
            card = commander_query.exclude(frame_effects__overlap=['extendedart','inverted']).order_by('released_at').first()
        try:
            is_commander_in_db = Commander.objects.get(commander_id=card.id)
            is_commander_in_db.card_list = item["deckList"]
            return item
        except Commander.DoesNotExist:
            commanderDeckList = Commander()
            commanderDeckList.commander = card
            commanderDeckList.name = card.name
            commanderDeckList.img_url = card.img_url
            commanderDeckList.card_list = item["deckList"]

            commanderDeckList.save()
            return item
