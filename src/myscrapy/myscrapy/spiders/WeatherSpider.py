#http://d1.weather.com.cn/sk_2d/101070101.html?_=1513091119303
import scrapy
import json
import re
from scrapy.http import Request
from myscrapy.items import WeatherItem
def str2Headers(file):
    headerDict = {}
    f = open(file,'r')
    headersText = f.read()
    # Windows：\r\n
    # Mac OS X、Linux：\n
    headers = re.split('\n',headersText)
    for header in headers:
        result = re.split(':',header,maxsplit=1)
        headerDict[result[0]] = result[1]
    f.close()
    return headerDict
class WeahterSpider(scrapy.Spider):
    name = 'WeatherSpider'
    def start_requests(self):
        headers = str2Headers('headers.txt')
        return [
            Request(url='http://d1.weather.com.cn/sk_2d/101070101.html?_=1513091119303',headers = headers)
            ]
    def parse(self,response):
        result = re.sub('var[ ]+dataSK[ ]+=[ ]+','',response.body.decode('utf-8'))
        jsonDict = json.loads(result)
        weatherItem = WeatherItem()
        for key,value in jsonDict.items():
            # 动态向WeatherItem中添加Field类型的属性
            weatherItem.fields[key] = scrapy.Field()
            weatherItem[key] = value
        return weatherItem
        