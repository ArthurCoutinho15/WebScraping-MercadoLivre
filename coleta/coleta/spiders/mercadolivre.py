import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0',
        'DEFAULT_REQUEST_HEADERS': {
            'Referer': 'https://www.google.com/',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
        }
    }

    def parse(self, response):
        products = response.css('div.ui-search-result__content')
        
        for product in products:
            yield {
                'brand': product.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get(),
                'name': product.css('h2.ui-search-item__title::text').get(),
            
            } 
            
            
    # entrar em coleta ao ativar o scrapy shell 
