# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YisaDaojuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    englishName = scrapy.Field()
    daojuUrl  = scrapy.Field()
    chineseName = scrapy.Field()
    imageName = scrapy.Field()
    imageUrl = scrapy.Field()
    daojuID = scrapy.Field()
    daojuChongneng = scrapy.Field()
    daojuXiaoguo = scrapy.Field()


class YisaShipinItem(scrapy.Item):
    shipinUrl = scrapy.Field()
    chineseName = scrapy.Field()
    imageName = scrapy.Field()
    imageUrl = scrapy.Field()
    shipinID = scrapy.Field()
    shipinXiaoguo = scrapy.Field()


class YisaWupinItem(scrapy.Item):
    wupinUrl = scrapy.Field()
    chineseName = scrapy.Field()
    imageName = scrapy.Field()
    imageUrl = scrapy.Field()
    wupinID = scrapy.Field()
    wupinXiaoguo = scrapy.Field()


class YisaYaowanItem(scrapy.Item):
    englishName = scrapy.Field()
    yaowanUrl = scrapy.Field()
    chineseName = scrapy.Field()
    yaowanID = scrapy.Field()
    yaowanXiaoguo = scrapy.Field()


class YisaChengjiuItem(scrapy.Item):
    chengjiuID = scrapy.Field()
    chengjiuUrl = scrapy.Field()
    chineseName = scrapy.Field()
    englishName = scrapy.Field()
    imageName = scrapy.Field()
    imageUrl = scrapy.Field()