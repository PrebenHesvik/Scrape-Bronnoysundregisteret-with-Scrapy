# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def add_country_code(value):
    return f'NO{value}MVA'.replace(' ', '')

class BrregScraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    vat_number = scrapy.Field(input_processor=MapCompose(remove_tags, add_country_code), output_processor=TakeFirst())
    address = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    municipality = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    postal_address = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
   
