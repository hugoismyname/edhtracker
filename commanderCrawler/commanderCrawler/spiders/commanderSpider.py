import scrapy
import json

from commanderCrawler.items import CommanderdataItem

from edhtracker.cards.models import Card


class CommanderSpider(scrapy.Spider):
    name = "commander"

    headers ={
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://edhrec.com/commanders",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }
    start_urls = [
        "https://edhrec.com/"
    ]
    commanderList = Card.objects.filter(is_commander=True).exclude(set_type="funny").exclude(set_type="memorabilia").order_by('name').distinct('name').values_list('name', flat=True)

    # marton stromgald fix
    
    def parse(self, response):
        for card in self.commanderList:
            urlCard = card.lower()
            try:
                urlCard = urlCard.replace("'","").replace(',', '').replace('"', '').replace('/', '').replace(':', '')
                urlCard = '-'.join(urlCard.split())
            except AttributeError:
                urlCard = '-'.join(card.split())
            url = f"https://edhrec-json.s3.amazonaws.com/en/commanders/{urlCard}.json"
            request = scrapy.Request(url,callback=self.parse_api,headers=self.headers,
                                        cb_kwargs=dict(commander=card))
            
            yield request

    def parse_api(self,response,commander):
        rawData = response.body
        deserializedData = json.loads(rawData)

        cardCatagories = deserializedData["container"]["json_dict"]["cardlists"]

        item = CommanderdataItem()
        item['commander'] = commander
        item['deckList'] = []
        for cardList in cardCatagories:
            for card in cardList["cardviews"]:
                item['deckList'].append(card["name"])  
        return  item