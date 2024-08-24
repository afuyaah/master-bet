import scrapy
from scrapy.http import Request
from app.scraper.scraper.items import SportsItem
from app import create_app, get_session
from app.main.models import ScrapedURL

class SportsSpider(scrapy.Spider):
    name = "sports_spider"
    allowed_domains = ["sofascore.com", "goal.com"]  # Add all necessary domains here

    def __init__(self, *args, **kwargs):
        super(SportsSpider, self).__init__(*args, **kwargs)
        self.app = create_app()  # Initialize Flask app
        self.session = None

    def start_requests(self):
        with self.app.app_context():
            self.session = get_session()
            urls = self.session.query(ScrapedURL.url).all()
            for url in urls:
                # Normalize URL by adding default scheme if missing
                url = url[0].strip()
                if not url.startswith(('http://', 'https://')):
                    url = 'http://' + url
                
                yield Request(url=url, callback=self.parse)

    def parse(self, response):
        for match in response.css('div.match'):
            item = SportsItem()
            item['team_a'] = match.css('div.team-a::text').get()
            item['team_b'] = match.css('div.team-b::text').get()
            item['score_a'] = match.css('div.score-a::text').get()
            item['score_b'] = match.css('div.score-b::text').get()
            item['date'] = match.css('div.date::text').get()
            yield item

        next_page = response.css('a.next-page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
