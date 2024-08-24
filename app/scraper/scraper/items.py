# app/scraping/scraper/items.py

import scrapy

class SportsItem(scrapy.Item):
    team_a = scrapy.Field()
    team_b = scrapy.Field()
    score_a = scrapy.Field()
    score_b = scrapy.Field()
    date = scrapy.Field()
