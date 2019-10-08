from scrapy import Item
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from picxel.items import PicxelItem


class MySpider(CrawlSpider):
    name = 'pic_spider'
    allowed_domains = ['wallpaperscraft.ru']
    start_urls = [
        'https://wallpaperscraft.ru/',
    ]
    rules = (
        Rule(LinkExtractor(allow='/wallpaper/'), callback='parse_item'),
    )

    def parse_item(self, response):
        item = PicxelItem()
        item['tags'] = response.xpath('//div[@class="wallpaper__tags"]/a/text()').getall()
        item['author'] = response.xpath('//div[@class="author__row"]/text()').get()
        item['license'] = response.xpath('//div[@class="author__row"]/span/text()').get()
        item['source'] = response.xpath('//a[@class="author__link"]/@href').get()
        item['pic_url'] = response.xpath('//a[@class="gui-button gui-button_full-height"]/@href').get()
        item['size'] = response.xpath('//a[@class="gui-button gui-button_full-height"]/@text').get()
        return item
