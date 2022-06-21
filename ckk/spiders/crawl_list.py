from ckk.items import SpiderItem
from ckk.spiders.utils import *

import scrapy

urls_to_crawl = get_updated_urls(load_urls())
class Knifekits(scrapy.Spider):
    name = "knifekits"
    start_urls = [url[0] for url in load_urls("https://www.knifekits.com/vcom/smproducts.xml")]

    def parse(self, response):
        base_url = "https://" + response.url.split('/')[2]+"/vcom/"
        item = SpiderItem()
        item["link"] = response.xpath('//*[@rel="canonical"]/@href').get()
        item["sku"] = response.xpath('//span[@itemprop="model"]/descendant-or-self::text()').get()
        item["name"] = response.xpath('//h1/descendant::span[@itemprop="name"]/text()').get()
        item["main_image"] = response.xpath('//div[@class="piGalMain"]/img/@src').get()
        item["products_id"] = response.xpath('//input[@name="products_id"]/@value').get()
        item["title"] = response.xpath("/html/head/title/text()").get()
        item["keywords"] = response.xpath('.//meta[@name="keywords"]/@content').get()
        item["short_desc"] = response.xpath('//meta[@name="description"]/@content').get()
        item["price"] = response.xpath('.//*[@itemprop="price"]/text()').get().replace('$','')
        item["description"] = response.xpath('//div[@itemprop="description"]').get()
        image_urls = [base_url+img for img in response.xpath('//*[@class="thumbnail"]/@data-image').getall()]
        bcrumbs = response.xpath('.//*[@class="breadcrumb"]/descendant-or-self::text()').getall()
        discount_tiers=response.xpath('.//*[@class="DiscountPriceQty"]/descendant-or-self::text()').getall()
        discount_amount=response.xpath('.//*[@class="DiscountPrice"]/descendant-or-self::text()').getall()
        item['image_urls'] = image_urls
        item['breadcrumbs'] = bcrumbs[::2]
        if len(discount_amount) <= 1 or len(discount_tiers) <= 1:
            item['discount_tiers'] = discount_tiers
            item['discount_amount'] = discount_amount
        if item['main_image'].startswith('images/'):
            item['main_image']=base_url + item['main_image']
        yield item

class Holstersmith(scrapy.Spider):
    name = "holstersmith"
    allowed_domains = ['holstersmith.com','localhost','127.0.0.1']
    start_urls = load_urls("https://www.holstersmith.com/vcom/smproducts.xml")[::2]
    # start_urls = get_updated_urls(load_urls())

    def parse(self, response):
        base_url = "https://" + response.url.split('/')[2]+"/vcom/"
        item = SpiderItem()
        item["link"] = response.xpath('//*[@rel="canonical"]/@href').get()
        item["sku"] = response.xpath('//span[@itemprop="model"]/descendant-or-self::text()').get()
        item["name"] = response.xpath('//h1/descendant::span[@itemprop="name"]/text()').get()
        item["main_image"] = response.xpath('//div[@class="piGalMain"]/img/@src').get()
        item["products_id"] = response.xpath('//input[@name="products_id"]/@value').get()
        item["title"] = response.xpath("/html/head/title/text()").get()
        item["keywords"] = response.xpath('.//meta[@name="keywords"]/@content').get()
        item["short_desc"] = response.xpath('//meta[@name="description"]/@content').get()
        item["price"] = response.xpath('.//*[@itemprop="price"]/text()').get().replace('$','')
        item["description"] = response.xpath('//div[@itemprop="description"]').get()
        image_urls = [base_url+img for img in response.xpath('//*[@class="thumbnail"]/@data-image').getall()]
        bcrumbs = response.xpath('.//*[@class="breadcrumb"]/descendant-or-self::text()').getall()
        discount_tiers=response.xpath('.//*[@class="DiscountPriceQty"]/descendant-or-self::text()').getall()
        discount_amount=response.xpath('.//*[@class="DiscountPrice"]/descendant-or-self::text()').getall()
        item['image_urls'] = image_urls
        item['breadcrumbs'] = bcrumbs[::2]
        if len(discount_amount) <= 1 or len(discount_tiers) <= 1:
            item['discount_tiers'] = discount_tiers
            item['discount_amount'] = discount_amount
        if item['main_image'].startswith('images/'):
            item['main_image']=base_url + item['main_image']
        
        yield item
