import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blog'
    start_urls = ['http://phonesdata.com/ru/smartphones/sony/#2019']

    def parse(self, response):
        # for title in response.css('.list-items::text').get():
        #     yield title

        for test in response.xpath("//p[@class='list-items']/a/text()").extract():
            yield test


# <p class = "list-items" >
