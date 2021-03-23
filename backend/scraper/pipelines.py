# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from django.conf import settings
import psycopg2

class ScraperPipeline:

    def open_spider(self, spider):
        hostname = settings.DATABASES.default.HOST
        username = settings.DATABASES.default.USER
        password = settings.DATABASES.default.PASSWORD
        database = settings.DATABASES.default.NAME
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("insert into quotes_content(content,author) values(%s,%s)",(item['content'],item['author']))
        self.connection.commit()
        return item
