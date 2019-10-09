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
        Rule(LinkExtractor(allow='/wallpaper/'), follow=True),
        Rule(LinkExtractor(allow='/download/', restrict_xpaths='//span[@class="wallpaper-table__cell"]/a'),
             callback='parse_item'),
    )

    def parse_item(self, response):
        item = PicxelItem()
        item['tags'] = response.xpath('//div[@class="wallpaper__tags"]/a/text()').getall()
        item['category'] = response.xpath('//div[@class="wallpaper__tags"]/a/text()').get()
        item['author'] = response.xpath('//div[@class="author__row"]/text()').get()
        item['license'] = response.xpath('//div[@class="author__row"]/span/text()').get()
        item['source'] = response.xpath('//a[@class="author__link"]/@href').get()
        item['pic_url'] = response.xpath('//a[@class="gui-button gui-button_full-height"]/@href').getall()
        item['size'] = response.xpath('//a[@class="gui-button gui-button_full-height"]/text()').get()
        return item
