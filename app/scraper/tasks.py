# app/scrapper/tasks.py

from app.extensions import celery
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .scraper.spiders.sports_spider import SportsSpider

@celery.task
def run_sports_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(SportsSpider)
    process.start()
