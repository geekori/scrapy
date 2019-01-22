import scrapy
from scrapy.http.request.form import FormRequest
class LoginSpider(scrapy.Spider):
    name = 'LoginSpider'
    def start_requests(self):
        return [
            FormRequest('http://localhost:5000/login',formdata={'username':'bill','password':'1234'},method='POST')
            ]
    def parse(self,response):
        print(response)
        text = response.xpath('//h1/text()').extract()
        print(text[0])
    