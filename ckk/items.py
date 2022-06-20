# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import re

from w3lib.html import remove_tags
import scrapy


def remove_html(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def get_updated_urls(tmp):
    r=[]
    now = arrow.utcnow()
    for i in tmp:
        if arrow.get(i[1]) >= now.shift(days=-15):
            # print(f"Link: {i} -- {arrow.get(i[1]).humanize()}")
            r.append(i[0])
    return r

def clean_description(desc):
    tmp = desc.replace("\t","").split('\r\n')
    new = [t.strip() for t in tmp]
    return new

class SpiderItem(scrapy.Item):
    link = scrapy.Field()
    sku = scrapy.Field()
    name = scrapy.Field()
    main_image = scrapy.Field()
    products_id = scrapy.Field()
    title = scrapy.Field()
    keywords = scrapy.Field()
    short_desc = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    description_text = scrapy.Field()
    image_urls = scrapy.Field()
    breadcrumbs = scrapy.Field()
    discount_tiers = scrapy.Field(deault='')
    discount_amount = scrapy.Field(default='')
    last_crawled = scrapy.Field()

    