# 使用ItemLoader保存多条抓取的数据（方法1）

import scrapy


class MultiUrlSpider(scrapy.Spider):
    name = 'MultiUrlSpider'
    start_urls = [
       url.strip() for url in open('./urls.txt').readlines()
        
    ]    
    def parse(self,response):
        sectionList = response.xpath('//*[@id="all"]/div[1]/section').extract()
        print('共有',len(sectionList),'条博文')
        
   
                
            
        

        
        
