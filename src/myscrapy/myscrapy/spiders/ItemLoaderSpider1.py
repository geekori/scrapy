# 使用ItemLoader保存多条抓取的数据（方法1）

import scrapy
from scrapy.loader import *
from scrapy.loader.processors import *
from bs4 import *
from myscrapy.items import MyscrapyItem
class ItemLoaderSpider1(scrapy.Spider):
    name = 'ItemLoaderSpider1'
    start_urls = [
        'https://geekori.com/blogsCenter.php?uid=geekori'
    ]
    def parse(self,response):
        items = []

        sectionList = response.xpath('//*[@id="all"]/div[1]/section').extract()
        for section in sectionList:
            bs = BeautifulSoup(section,'lxml')
            articleDict = {}
            a = bs.find('a')
            
            articleDict['title'] = a.text
            articleDict['href'] = 'https://geekori.com/' + a.get('href')
            p = bs.find('p',class_='excerpt')
            articleDict['abstract'] = p.text
            itemLoader = ItemLoader(item = MyscrapyItem(),response = response)
            itemLoader.add_value('title', articleDict['title'])
            itemLoader.add_value('href', articleDict['href'])
            itemLoader.add_value('abstract', articleDict['abstract'])
            items.append(itemLoader.load_item())
      
        return items  
