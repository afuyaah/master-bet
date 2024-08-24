# app/scrapper/routes.py

from flask import Blueprint, jsonify
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .scraper.spiders.sports_spider import SportsSpider

scraping_bp = Blueprint('scraping', __name__)

@scraping_bp.route('/scrape', methods=['GET'])
def start_scraping():
    run_sports_spider.delay()
    return jsonify({"status": "Scraping task started!"})
