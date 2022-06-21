import re

from requests_html import HTMLSession
import arrow


now = arrow.now()

def load_urls(url="https://knifekits.com/vcom/smproducts.xml"):
    session = HTMLSession()
    page = session.get(url)
    tmp = {}
    
    tmp['urls'] = page.html.xpath('//loc/text()')
    tmp['stamps'] = page.html.xpath('//lastmod/text()')
    return list(zip(tmp['urls'],tmp['stamps']))

def new_load_urls(url="https://knifekits.com/vcom/smproducts.xml", urls=False, stamps=False):
    """
    Returns a list of urls and timestamps from the sitemap.
    if urls or stamps is set to True:
        returns only a list of urls or stamps
    if both are set to True:
        Evil wins.
    """
    session = HTMLSession()
    page = session.get(url)
    txt = page.html.xpath('//url/descendant-or-self::text()')
    if urls and stamps:
        print("Evil!")
        return txt
    elif urls is True:
        return txt[::2]
    elif stamps is True:
        return txt[1::2]
    return page

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

fields={
    "link": '//*[@rel="canonical"]/@href',
    "sku": '//span[@itemprop="model"]/descendant-or-self::text()',
    "name": '//h1/descendant::span[@itemprop="name"]/text()',
    "main_image": '//div[@class="piGalMain"]/img/@src',
    "products_id": '//input[@name="products_id"]/@value',
    "title": "/html/head/title/text()",
    "keywords": './/meta[@name="keywords"]/@content',
    "short_desc": '//meta[@name="description"]/@content',
    "price": './/*[@itemprop="price"]/text()',
    "description": '//div[@itemprop="description"]'}

list_fields = {
    "image_urls": '//*[@class="thumbnail"]/@data-image',
    "breadcrumbs": './/*[@class="breadcrumb"]/descendant-or-self::text()',
    "discount_tiers": './/*[@class="DiscountPriceQty"]/descendant-or-self::text()',
    "discount_amount": './/*[@class="DiscountPrice"]/descendant-or-self::text()'
}
