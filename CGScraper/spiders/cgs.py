import scrapy
import logging


class CgsSpider(scrapy.Spider):
    name = 'cgs'
    allowed_domains = ['gazette.gc.ca']
    start_urls = ['https://www.gazette.gc.ca/rp-pr/p1/2021/index-eng.html']

    def parse(self, response):
        baseurl = 'https://www.gazette.gc.ca'
        for link in response.xpath('//td[4]'):
            yield {
                'part': link.xpath('a/text()').getall()[0].replace('\xa0', ' ').replace(',',"").strip(),
                'volume': link.xpath('a/text()').getall()[1].replace(',',"").strip(),
                'number': link.xpath('a/text()').getall()[2].replace(',',"").strip(),
                'url': baseurl + link.xpath('a/@href').get()
            }