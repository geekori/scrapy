import scrapy
from scrapy.http.request.form import FormRequest
from _cffi_backend import callback
class LoginSpider1(scrapy.Spider):
    name = 'LoginSpider1'

    def start_requests(self):
        return [
            # 相当于用浏览器访问该页面
            FormRequest('http://localhost:5000/static/login1.html', callback=self.parseLogin)
        ]

    def parseLogin(self, response):
        return FormRequest.from_response(response, formdata={'username': 'bill', 'password': '1234'})

    def parse(self, response):
        print(response)
        text = response.xpath('//h1/text()').extract()
        print(text[0])
