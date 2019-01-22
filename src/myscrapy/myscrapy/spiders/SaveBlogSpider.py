import scrapy
from bs4 import *
from myscrapy.items import MyscrapyItem


class SaveBlogSpider(scrapy.Spider):
    name = 'SaveBlogSpider'
    start_urls = [
        'https://geekori.com/blogsCenter.php?uid=geekori'
        ]
    def parse(self,response):
        # 创建MyscrapyItem类的实例
        item = MyscrapyItem()
        sectionList = response.xpath('//*[@id="all"]/div[1]/section').extract()
        for section in sectionList:
            bs = BeautifulSoup(section,'lxml')
            articleDict = {}
            a = bs.find('a')
            articleDict['title'] = a.text
            articleDict['href'] = 'https://geekori.com/' + a.get('href')
            p = bs.find('p', class_='excerpt')
            articleDict['abstract'] = p.text
            # 为MyscrapyItem对象的3个属性赋值
            item['title'] = articleDict['title']
            item['href'] = articleDict['href']
            item['abstract'] = articleDict['abstract']
            # 本例只保存抓取的第1条博文先关信息，所以迭代一次后退出for循环
            break
            # 返回MyscrapyItem对象
        return item
