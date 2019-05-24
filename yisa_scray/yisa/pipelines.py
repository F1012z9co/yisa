# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from yisa.items import YisaDaojuItem, YisaShipinItem, YisaWupinItem, YisaYaowanItem, YisaChengjiuItem

class YisaPipeline(object):

    def __init__(self):
        self.db = pymysql.connect('localhost','root','FHzy1012','yisa',charset='utf8')
        self.conn = self.db.cursor()

    def open_spider(self, spider):
        print('spider启动')


    def process_item(self, item, spider):
        # print(dir(item))
        # print(','.join(item.keys()))
        # print(','.join(item.values()))
        # sql = '''INSERT INTO daoju({}) VALUES("{}")'''.format(','.join(item.keys()), '","'.join(item.values()))
        # print(sql)

        if isinstance(item,YisaDaojuItem):
            sql = '''INSERT INTO quickstart_daoju({}) VALUES("{}")'''.format(','.join(item.keys()), '","'.join(item.values()))
            print(sql)
            self.conn.execute(sql)
            self.db.commit()
            return item
        elif isinstance(item,YisaShipinItem):
            sql = '''INSERT INTO quickstart_shipin({}) VALUES("{}")'''.format(','.join(item.keys()), '","'.join(item.values()))
            self.conn.execute(sql)
            self.db.commit()
            return item
        elif isinstance(item, YisaWupinItem):
            sql = '''INSERT INTO quickstart_wupin({}) VALUES("{}")'''.format(','.join(item.keys()), '","'.join(item.values()))
            self.conn.execute(sql)
            self.db.commit()
            return item
        elif isinstance(item, YisaYaowanItem):
            sql = '''INSERT INTO quickstart_yaowan({}) VALUES("{}")'''.format(','.join(item.keys()), '","'.join(item.values()))
            self.conn.execute(sql)
            self.db.commit()
            return item
        elif isinstance(item, YisaChengjiuItem):
            sql = '''INSERT INTO quickstart_chengjiu({}) VALUES("{}")'''.format(','.join(item.keys()), '","'.join(item.values()))
            self.conn.execute(sql)
            self.db.commit()
            return item

    def close_spider(self,spider):
        self.conn.close()
        self.db.close()
        print('spider关闭')


'''

create table daoju (id int auto_increment primary key,englishName text,daojuUrl text,chineseName text, imageNametext, imageUrl text,daojuID text,daojuChongneng text, daojuXiaoguo text)


create table shipin (id int auto_increment primary key,shipinUrl text, chineseName text,imageName text, imageUrl text, shipinID text, shipinXiaoguo text)


create table wupin ( id int auto_increment primary key,wupinUrl text, chineseName text, imageName text, imageUrl text, wupinID text ,wupinXiaoguo text)


create table yaowan( id int auto_increment primary key , englishName text, yaowanUrl text, chineseName text, yaowanID text, yaowanXiaoguo text)


create table chengjiu(id int auto_increment primary key,chengjiuID text, chengjiuUrl text, chineseName text,englishName text, imageName text, imageUrl text)
'''

