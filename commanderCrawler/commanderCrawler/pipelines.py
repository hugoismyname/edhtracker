# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


from edhtracker.cards.models import Commander
from edhtracker.cards.models import Card

class CommandercrawlerPipeline(object):
    def process_item(self, item, spider):
        commander_query = Card.objects.filter(name__icontains=item['commander'])
        commander_query = commander_query.filter(is_commander=True)
        for card in commander_query:
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

