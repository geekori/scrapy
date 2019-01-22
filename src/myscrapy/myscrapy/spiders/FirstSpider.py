import scrapy
class FirstSpider(scrapy.Spider):
    # Spider的名称，需要该名称启动Scrapy
    name = 'FirstSpider'
    # 指定要抓取的Web资源的Url
    start_urls = [
        'https://www.jd.com'
        ]
    # 每抓取一个Url对应的Web资源，就会调用该方法，通过response参数可以执行XPath过滤标签
    def parse(self,response):
    # 输出日期信息
        self.log('hello world')
