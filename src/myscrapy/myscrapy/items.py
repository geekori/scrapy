# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    # 每一个要保存的属性都必须是Field类的实例
    title = scrapy.Field()
    href = scrapy.Field()
    abstract = scrapy.Field()

class CommentItem(scrapy.Item):
    productId = scrapy.Field()
    content = scrapy.Field()
    productColor = scrapy.Field()
    creationTime = scrapy.Field()
class BookItem(scrapy.Item):
    title = scrapy.Field()
    press = scrapy.Field()
    ISBN = scrapy.Field()
    productId = scrapy.Field()
class BookItem1(scrapy.Item):
    pass
class NewBookItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    press = scrapy.Field()
    ISBN = scrapy.Field()
    productId = scrapy.Field()
class WeatherItem(scrapy.Item):
    pass

class NewBookItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    press = scrapy.Field()
    ISBN = scrapy.Field()
    productId = scrapy.Field()
class BookItem1(scrapy.Item):
    pass