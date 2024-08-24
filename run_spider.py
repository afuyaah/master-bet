# run_spider.py

from scrapy.crawler import CrawlerProcess
from app.scraper.scraper.spiders.sports_spider import SportsSpider

def run_spider():
    process = CrawlerProcess(settings={
        "FEEDS": {
            "output.json": {"format": "json"},
        },
        "LOG_LEVEL": "DEBUG",  # Optional: Adjust log level if needed
    })

    process.crawl(SportsSpider)
    process.start()

if __name__ == "__main__":
    run_spider()
