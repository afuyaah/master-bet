# app/scrapper/scrapper/pipelines.py

import psycopg2

class SportsPipeline:
    def open_spider(self, spider):
        self.conn = psycopg2.connect("dbname=yourdbname user=youruser password=yourpassword host=yourhost")
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        self.cur.execute("""
            INSERT INTO sports_data (team_a, team_b, score_a, score_b, date)
            VALUES (%s, %s, %s, %s, %s)
        """, (item['team_a'], item['team_b'], item['score_a'], item['score_b'], item['date']))
        self.conn.commit()
        return item
