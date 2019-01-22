import scrapy
from myscrapy.items import NewBookItem

from scrapy.conf import settings
import re
class BookSpider(scrapy.Spider):
    name = 'BookSpider'

    settings.set('CONCURRENT_REQUESTS',100)

    def start_requests(self):
        return [
            scrapy.Request('https://search.jd.com/Search?keyword=python&enc=utf-8&wq=python&pvid=186e2514605040b4987bfc7a62e3d5e0',callback=self.parseBookList)
            ]
    def parseBookList(self,response):       
        hrefs = response.xpath('//*[@id="J_goodsList"]/ul/li/div/div[1]/a/@href[starts-with(.,"//item.jd.com/")]').extract()
        for href in hrefs:
            result = re.match('.*/(\d+).*',href)
            productId = result.group(1)
            yield scrapy.Request('https:' + href,meta={'productId':productId,'url':'https:' + href},callback=self.parseBook)
    def parseBook(self, response):
        values = response.xpath('//*[@id="name"]/div[1]/text()').extract()
        title = ''
        for value in values:
            title += value
        title =  title.strip()
        press = response.xpath('//*[@id="parameter2"]/li[1]/a/text()').extract()[0]
        ISBN = response.xpath('//*[@id="parameter2"]/li[2]/@title').extract()[0]
        productId = response.meta['productId']
        url = response.meta['url']
        bookItem = NewBookItem()
        bookItem['url'] = url
        bookItem['title'] = title
        bookItem['press'] = press
        bookItem['ISBN'] = ISBN
        bookItem['productId'] = productId
        return bookItem
