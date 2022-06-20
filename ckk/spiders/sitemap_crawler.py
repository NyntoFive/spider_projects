
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