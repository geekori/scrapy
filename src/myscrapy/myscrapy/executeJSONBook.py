from scrapy import cmdline
cmdline.execute('scrapy crawl ToJSONSpider -o books.jl'.split())