import scrapy

class MyspiderSpider(scrapy.Spider):
    name = "myspider"

    def start_requests(self):
        url = 'https://candelamedical.com/patient/find-a-provider/?country=United+States&distance=25&unit=m&address=94112&cf=find&treatment=any&brand=9'
        # params = {
        #     'country': 'United States',
        #     'distance': '25',
        #     'unit': 'm',
        #     'address': '94112',
        #     'cf': 'find',
        #     'treatment': 'any',
        #     'brand': '9',
        # }
        # params = {
        #     'brand': '',
        #     'cf': 'find',
        #     'country': 'United States',
        #     'address': '94112',
        #     'treatment': 'any',
        #     'distance': '25',
        #     'unit': 'mi',
        # }
        # headers = {
        #     'authority': 'candelamedical.com',
        #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        #     'accept-language': 'en',
        #     'cookie': '_gcl_au=1.1.1036559884.1712691458; _omappvp=r5QynhWmu0gEWqdXR2FGLhus4IewGc7fRIYqDs2WFR6Uy62zXA4gD2ezA4cVbXK6oh6pSV5CXebUnVZoBP5sjNsEm8D6jTs4; _biz_uid=2587b61a41dd4401b94f1c8ad3d6affc; _mkto_trk=id:620-HCU-218&token:_mch-candelamedical.com-1712691462670-52455; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22Mkto%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; _fbp=fb.1.1712691463696.1855001095; _gid=GA1.2.1910693231.1712956334; _gat_UA-190145697-2=1; arp_scroll_position=403; _biz_nA=4; _biz_pendingA=%5B%5D; _ga=GA1.2.878774029.1712691461; _ga_FCX99HCS7V=GS1.1.1712956334.2.1.1712956371.23.0.318828434; _ga_630HCMSM4C=GS1.1.1712956334.2.1.1712956371.23.0.0',
        #     'referer': 'https://candelamedical.com/patient/find-a-provider/?country=United+States&distance=25&unit=m&address=94112&cf=find&treatment=any&brand=9',
        #     'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        #     'sec-ch-ua-mobile': '?0',
        #     'sec-ch-ua-platform': '"macOS"',
        #     'sec-fetch-dest': 'document',
        #     'sec-fetch-mode': 'navigate',
        #     'sec-fetch-site': 'same-origin',
        #     'sec-fetch-user': '?1',
        #     'upgrade-insecure-requests': '1',
        #     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        # }
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        cards=response.xpath('//div[@result]')
        print(len(cards))
