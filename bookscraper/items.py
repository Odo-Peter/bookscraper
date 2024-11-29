# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class BookscraperItem(Item):
    # define the fields for your item here like:
    title = Field()
    price = Field()
    # upc = Field()
    image_url = Field()
    url = Field()
    pass
