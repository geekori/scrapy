import scrapy
from bs4 import *
class BlogSpider(scrapy.Spider):
    name = 'BlogSpider'
    start_urls = [
        'https://geekori.com/blogsCenter.php?uid=geekori'
        ]
    def parse(self,response):
        # 过滤出指定页面所有的博文
            sectionList = response.xpath('//*[@id="all"]/div[1]/section').extract()
            # 对博文列表进行迭代
            for section in sectionList:
                # 利用BeautifulSoup对每一篇博文的相关信息进行过滤
                bs = BeautifulSoup(section,'lxml')
                articleDict = {}
                a = bs.find('a')
                # 获取博文标题
                articleDict['title'] = a.text
                # 获取博文的Url
                articleDict['href'] = 'https://geekori.com/' + a.get('href')
                p = bs.find('p', class_='excerpt')
                # 获取博文的摘要
                articleDict['abstract'] = p.text
                print(articleDict)

