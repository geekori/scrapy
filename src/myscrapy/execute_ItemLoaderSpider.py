from scrapy import cmdline
# 通过代码运行基于Scrapy框架的网络爬虫
cmdline.execute('scrapy crawl ItemLoaderSpider -o item1.json'.split())
