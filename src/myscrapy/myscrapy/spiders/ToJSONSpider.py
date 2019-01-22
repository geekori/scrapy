import scrapy
from myscrapy.items import BookItem1
import csv
class toJSONSpider(scrapy.Spider):
    name = 'ToJSONSpider'
    def start_requests(self):
        with open('books.csv','r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for line in reader:
                url = line['url']
                request = scrapy.Request(url)
                request.meta['fields'] = line

                yield request
    def parse(self,response):

        bookItem = BookItem1()
        for name,value in response.meta['fields'].items():
            bookItem.fields[name] = scrapy.Field()
            bookItem[name] = value
        return bookItem
        

        