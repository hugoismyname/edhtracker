# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from edhtracker.cards.models import Commander
from edhtracker.cards.models import Card

class CommanderCrawlerPipeline(object):
    def process_item(self, item, spider):
        # get all commanders matching name 
        commander_query = Card.objects.filter(name=item['commander'])
        for card in commander_query:
            try:
                is_commander_in_db = Commander.objects.get(commander_id=card.id)
                is_commander_in_db.card_list = item['deckList']
                is_commander_in_db.save()
            except Commander.DoesNotExist:
                commanderDeckList = Commander()
                # foreign key relation on card
                commanderDeckList.commander = card
                commanderDeckList.name = card.name
                commanderDeckList.img_url = card.img_url
                commanderDeckList.card_list = item['deckList']

                commanderDeckList.save()

