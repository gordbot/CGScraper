import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

# def encodeUTF8(string):
    # return string.encode('latin-1').decode('unicode_escape').encode('latin-1').decode()('utf-8').strip()

class LinkItem(scrapy.Item):
    text = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    url = scrapy.Field()
