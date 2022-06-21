# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import re
import arrow
from typing import Optional, List, Any, Union
from pydantic import BaseModel, Field, HttpUrl, condecimal
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
    products_id = scrapy.Field(default="-1")
    title = scrapy.Field()
    keywords = scrapy.Field()
    short_desc = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    description_text = scrapy.Field()
    image_urls = scrapy.Field()
    breadcrumbs = scrapy.Field()
    discount_tiers = scrapy.Field()
    discount_amount = scrapy.Field()
    last_crawled = scrapy.Field()

    def strip_desc(self, **kwargs):
        
        desc = remove_html(self.description).replace('\t','').replace('\xa0',' ').split('\r\n')
        return desc


class KnifekitsItem(BaseModel):
    link: HttpUrl
    sku: str
    name: str
    main_image: HttpUrl
    products_id: Optional[Union[str, int]]
    title: Optional[str]
    keywords: Optional[Union[List[str], str]]
    short_desc: Optional[str]
    price: Optional[Union[condecimal(max_digits=2, decimal_places=2), str]]
    description: Optional[Any]
    image_urls: Optional[Union[List[HttpUrl], str]]
    breadcrumbs: Optional[List[str]]
    discount_tiers: Optional[List[str]]
    discount_amount: Optional[List[str]]
