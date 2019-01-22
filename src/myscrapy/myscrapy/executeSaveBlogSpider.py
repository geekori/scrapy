from scrapy import cmdline
# 将抓取的数据保存为json格式的文件（blog.json）
cmdline.execute('scrapy crawl SaveBlogSpider -o blog.json'.split())
