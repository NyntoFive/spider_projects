
    # def parse(self, response):
    #     item = SpiderItem()
    #     for k,v in fields.items():
    #         item[k] = response.xpath(v).get()
    #     for k,v in list_fields.items():
    #         item[k] = response.xpath(v).getall()
    #     base_url = "https://" + response.url.split('/')[2]+"/vcom/"
        
    #     if item.get('image_urls'):
    #         item['image_urls'] = ["https://" + response.url.split('/')[2]+"/vcom/" + img for img in item['image_urls']]
    #         item['main_image'] = base_url + item['main_image']
    #     if "$" in item['price']:
    #         item['price'] = item['price'].replace('$','')
    #     if "Home" in item['breadcrumbs'][0]:
    #         item['breadcrumbs'] = item['breadcrumbs'][4::2]
    #     item['description_text'] = remove_html("\n".join(clean_description(item['description'])))

    #     if len(item['discount_amount'])>=1 and "$" in item['discount_amount'][0]:
    #         item['discount_amount'] =  [i.replace('$','').strip() for i in item['discount_amount']]
    #     item['last_crawled'] = arrow.now().date()

    #     yield item

    

# def alternate_parse(self, response):
#         base_url = "https://" + response.url.split('/')[2]+"/vcom/"
#         item = CrawlerItem()
#         item["link"] = response.xpath('//*[@rel="canonical"]/@href').get()
#         item["sku"] = response.xpath('//span[@itemprop="model"]/descendant-or-self::text()').get()
#         item["name"] = response.xpath('//h1/descendant::span[@itemprop="name"]/text()').get()
#         item["main_image"] = response.xpath('//div[@class="piGalMain"]/img/@src').get()
#         item["products_id"] = response.xpath('//input[@name="products_id"]/@value').get()
#         item["title"] = response.xpath("/html/head/title/text()").get()
#         item["keywords"] = response.xpath('.//meta[@name="keywords"]/@content').get()
#         item["short_desc"] = response.xpath('//meta[@name="description"]/@content').get()
#         item["price"] = response.xpath('.//*[@itemprop="price"]/text()').get().replace('$','')
#         item["description"] = response.xpath('//div[@itemprop="description"]').get()
#         image_urls = [base_url+img for img in response.xpath('//*[@class="thumbnail"]/@data-image').getall()]
#         bcrumbs = response.xpath('.//*[@class="breadcrumb"]/descendant-or-self::text()').getall()
#         discount_tiers=response.xpath('.//*[@class="DiscountPriceQty"]/descendant-or-self::text()').getall()
#         discount_amount=response.xpath('.//*[@class="DiscountPrice"]/descendant-or-self::text()').getall()
#         item['image_urls'] = image_urls
#         item['breadcrumbs'] = bcrumbs[::2]
#         if len(discount_amount) >= 1 or len(discount_tiers) >= 1:
#             item['discount_tiers'] = discount_tiers
#             item['discount_amount'] = discount_amount
#         if item['main_image'].startswith('images/'):
#             item['main_image']=base_url + item['main_image']
#         yield item
