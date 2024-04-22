import json
import scrapy


class Myspider2Spider(scrapy.Spider):
    name = "myspider2"
    # allowed_domains = ["X"]
    # start_urls = ["https://X"]
    custom_settings = {
     
        'ZYTE_API_KEY' : "862fc22d70de4b7eb023644a667ef9c1",
        'DOWNLOAD_HANDLERS': {
            "http": "scrapy_zyte_api.ScrapyZyteAPIDownloadHandler",
            "https": "scrapy_zyte_api.ScrapyZyteAPIDownloadHandler",
        },
        'DOWNLOADER_MIDDLEWARES':{
            "scrapy_zyte_api.ScrapyZyteAPIDownloaderMiddleware": 1000,
        },
        'REQUEST_FINGERPRINTER_CLASS' :"scrapy_zyte_api.ScrapyZyteAPIRequestFingerprinter",
        'SPIDER_MIDDLEWARES' : {
            "scrapy_zyte_api.ScrapyZyteAPISpiderMiddleware": 100,
        }
        
    }
    def start_requests(self):
        
        yield scrapy.Request("https://www.arielpremium.com/product-search?showAll=Y&page=1&searchTerm=&min=&max=")
    def parse(self, response):
        print(response.status)
        pass
