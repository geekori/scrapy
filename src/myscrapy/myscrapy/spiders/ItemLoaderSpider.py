# 使用ItemLoader返回单个Item

import scrapy
from scrapy.loader import *
from scrapy.loader.processors import *
from bs4 import *
from myscrapy.items import MyscrapyItem
class ItemLoaderSpider(scrapy.Spider):
    name = 'ItemLoaderSpider'
    start_urls = [
        'https://geekori.com/blogsCenter.php?uid=geekori'
    ]
    def parse(self,response):
        itemLoader = ItemLoader(item = MyscrapyItem(),response=response)
        itemLoader.add_xpath('title', '//*[@id="all"]/div[1]/section[1]/div[2]/h2/a/text()')
        itemLoader.add_xpath('href', '//*[@id="all"]/div[1]/section[1]/div[2]/h2/a/@href',MapCompose(lambda href:'https://geekori.com/' + href))
        itemLoader.add_xpath('abstract','//*[@id="all"]/div[1]/section[1]/div[2]/p/text()')
        return itemLoader.load_item()
