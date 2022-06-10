# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 设置要存储的字段
    # _id太重要了，一定保留
    _id = scrapy.Field()
    title = scrapy.Field()
    rating_num = scrapy.Field()

