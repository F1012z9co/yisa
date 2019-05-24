# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from yisa.items import YisaDaojuItem, YisaShipinItem, YisaWupinItem, YisaYaowanItem, YisaChengjiuItem

class YisaspiderSpider(scrapy.Spider):
    name = 'yisaSpider'
    allowed_domains = ['isaac.huijiwiki.com']
    start_urls = ['http://isaac.huijiwiki.com/']



    def start_requests(self):
        urls = [
            'https://isaac.huijiwiki.com/wiki/%E9%81%93%E5%85%B7',
            'https://isaac.huijiwiki.com/wiki/%E9%A5%B0%E5%93%81',
            'https://isaac.huijiwiki.com/wiki/%E5%8D%A1%E7%89%8C',
            'https://isaac.huijiwiki.com/wiki/%E8%8D%AF%E4%B8%B8',
            'https://isaac.huijiwiki.com/wiki/%E6%88%90%E5%B0%B1'
        ]
        for index,url in enumerate(urls):
            if index == 0:
                yield scrapy.Request(url, callback=self.daoju_parse)
            elif index == 1:
                yield scrapy.Request(url, callback=self.shipin_parse)
            elif index == 2:
                yield scrapy.Request(url, callback=self.wupin_parse)
            elif index == 3:
                yield scrapy.Request(url, callback=self.yaowan_parse)
            elif index == 4:
                yield scrapy.Request(url, callback=self.chengjiu_parse)



    def daoju_parse(self, response):
        daoju_dist = YisaDaojuItem()
        wikiTable = response.xpath('//table[@class="wikitable sortable table-striped mw-collapsible"]').re(r'<td>(.*?)<br><a href="(.*?)" .*?>(.*?)</a></td><td align="center"><a.*?><img alt="(.*?)" src="(.*?)".*?></a></td><td align="right">(.*?)</td>.*?<span .*?>(.*?)</span></td><td>(.*?)</td>')
        yisaLists = [wikiTable[i:i+8] for i in range(0, len(wikiTable), 8)]
        for daoju in yisaLists:
            daoju_dist['englishName'] = daoju[0]
            daoju_dist['daojuUrl'] = urljoin('https://isaac.huijiwiki.com',daoju[1])
            daoju_dist['chineseName'] = daoju[2]
            daoju_dist['imageName'] = daoju[3]
            daoju_dist['imageUrl'] = urljoin('https://isaac.huijiwiki.com',daoju[4])
            daoju_dist['daojuID'] = daoju[5]
            daoju_dist['daojuChongneng'] = daoju[6]
            daoju_dist['daojuXiaoguo'] = daoju[7]
            yield daoju_dist


    def shipin_parse(self, response):
        shipin_dist = YisaShipinItem()
        wikiTable = response.xpath('//table[@class="wikitable sortable table-striped mw-collapsible"]').re(r'<td><a href="(.*?)".*?>(.*?)</a></td>.*?<img alt="(.*?)" src="(.*?)" .*?<td align="right">(.*?)</td><td>(.*?)</td>')
        yisaLists = [wikiTable[i:i+6] for i in range(0, len(wikiTable), 6)]
        for shipin in yisaLists:
            shipin_dist['shipinUrl'] = urljoin('https://isaac.huijiwiki.com',shipin[0])
            shipin_dist['chineseName'] = shipin[1]
            shipin_dist['imageName'] = shipin[2]
            shipin_dist['imageUrl'] = urljoin('https://isaac.huijiwiki.com',shipin[3])
            shipin_dist['shipinID'] = shipin[4]
            shipin_dist['shipinXiaoguo'] = shipin[5]
            yield shipin_dist

    def wupin_parse(self, response):
        wupin_dist = YisaWupinItem()
        wikiTable = response.xpath('//table[@class="wikitable sortable table-striped mw-collapsible"]').re(r'<td><a href="(.*?)".*?>(.*?)</a>.*?<img alt="(.*?)" src="(.*?)".*?<td align="right">(.*?)</td><td>(.*?)</td>')
        yisaLists = [wikiTable[i:i + 6] for i in range(0, len(wikiTable), 6)]
        # print(yisaLists)
        for wupin in yisaLists:
            wupin_dist['wupinUrl'] = urljoin('https://isaac.huijiwiki.com',wupin[0])
            wupin_dist['chineseName'] = wupin[1]
            wupin_dist['imageName'] = wupin[2]
            wupin_dist['imageUrl'] = urljoin('https://isaac.huijiwiki.com',wupin[3])
            wupin_dist['wupinID'] = wupin[4]
            wupin_dist['wupinXiaoguo'] = wupin[5]
            yield wupin_dist

    def yaowan_parse(self, response):
        yaowan_dist = YisaYaowanItem()
        wikiTable = response.xpath('//table[@class="wikitable sortable table-striped mw-collapsible"]').re(r'<td>(.*?)<br><a href="(.*?)".*?>(.*?)</a></td><td align="right">(.*?)</td><td>(.*?)</td>')
        # print(wikiTable)
        yisaLists = [wikiTable[i:i + 5] for i in range(0, len(wikiTable), 5)]
        # print(yisaLists)
        for yaowan in yisaLists:
            yaowan_dist['englishName'] = yaowan[0]
            yaowan_dist['yaowanUrl'] = urljoin('https://isaac.huijiwiki.com',yaowan[1])
            yaowan_dist['chineseName'] = yaowan[2]
            yaowan_dist['yaowanID'] = yaowan[3]
            yaowan_dist['yaowanXiaoguo'] = yaowan[4]
            yield yaowan_dist

    def chengjiu_parse(self, response):
        chengjiu_dist = YisaChengjiuItem()
        wikiTable = response.xpath('//table[@class="wikitable sortable"]')[0].re(r'<td>(.*?)</td><td><a href="(.*?)" title=".*?">(.*?)</a><br>(.*?)</td><td><a href=.*?><img alt="(.*?)" src="(.*?)" .*?></a></td><td>.*?</td><td>.*?</td><td>.*?</td>')
        yisaLists = [wikiTable[i:i + 6] for i in range(0, len(wikiTable), 6)]
        for chengjiue in yisaLists:
            chengjiu_dist['chengjiuID'] = chengjiue[0]
            chengjiu_dist['chengjiuUrl'] = urljoin('https://isaac.huijiwiki.com',chengjiue[1])
            chengjiu_dist['chineseName'] = chengjiue[2]
            chengjiu_dist['englishName'] = chengjiue[3]
            chengjiu_dist['imageName'] = chengjiue[4]
            chengjiu_dist['imageUrl'] = urljoin('https://isaac.huijiwiki.com',chengjiue[5])
            yield chengjiu_dist