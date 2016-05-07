# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector

from taoqi.items import TaoqiItem



class SpiderTaoqiSpider(Spider):
    name = "taoqi"
    allowed_domains = ["tqmall.com"]
    start_urls = range(10000,11000)
    start_urls = ['http://www.tqmall.com/Goods/detail.html?id='+str(x) for x in start_urls]

    # def start_requests(self): #构造开始request
    #     for url in self.start_urls:
    #         yield self.make_requests_from_url(url)   #返回一个request的生成器


    def parse(self, response):
        sel = Selector(response)
        title = sel.xpath('//div[@class="title-product"]/text()')
        item = TaoqiItem()
        item['name'] = title.extract()

        return item

    # def make_requests_from_url(self, url):
    #     while (self.pno < 10000):
    #         self.pno += 1
    #         url += str(self.pno)
