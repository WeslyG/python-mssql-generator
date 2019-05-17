# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['phonesdata.com']
    start_urls = ['http://phonesdata.com/ru/smartphones/']

    def parse(self, response):
        # get all categories
        result = []
        text = response.xpath(
            "//a[starts-with(@href, 'http://phonesdata.com/ru/smartphones')]/text()").extract()
        for i in text:
          if "\n" not in i:
            if i not in result:
              result.append(i)
        print(result)

        for i in result:
            data = response.xpath("//p[@class='list-items']/a/text()").extract()
            print(data)
