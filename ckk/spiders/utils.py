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
def cleanup_description(s):
    """ Takes a string and cleans it by removing newline, tab and whitespace.
    @param s: Any string
    @return: Cleaned up string
    """
    if s:
        r=[line.replace('\t','') for line in s]
        tmp=" ".join(r)


        r = '\r\n'.join([x.strip() for x in r])
        if r:
            r = r.replace('\xa0', ' ')  # &nbsp to space
        return r
    else:
        return None
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


def alternate_parse(self, response):
        base_url = "https://" + response.url.split('/')[2]+"/vcom/"
        item = CrawlerItem()
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
        if len(discount_amount) >= 1 or len(discount_tiers) >= 1:
            item['discount_tiers'] = discount_tiers
            item['discount_amount'] = discount_amount
        if item['main_image'].startswith('images/'):
            item['main_image']=base_url + item['main_image']
        yield item
