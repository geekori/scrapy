from scrapy import cmdline
cmdline.execute('scrapy crawl BookSpider -o books.csv'.split())