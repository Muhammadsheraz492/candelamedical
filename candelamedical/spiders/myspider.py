import json

import scrapy
import csv
class MyspiderSpider(scrapy.Spider):
    name = "myspider"

    def start_requests(self):
        state_zipcodes = {
            "Alabama": "35004",
            "Alaska": "99501",
            "Arizona": "85001",
            "Arkansas": "72201",
            "California": "94112",
            "Colorado": "80201",
            "Connecticut": "06101",
            "Delaware": "19901",
            "Florida": "33101",
            "Georgia": "30301",
            "Hawaii": "96801",
            "Idaho": "83701",
            "Illinois": "60601",
            "Indiana": "46201",
            "Iowa": "50301",
            "Kansas": "66101",
            "Kentucky": "40201",
            "Louisiana": "70112",
            "Maine": "04101",
            "Maryland": "21201",
            "Massachusetts": "02101",
            "Michigan": "48201",
            "Minnesota": "55101",
            "Mississippi": "39201",
            "Missouri": "63101",
            "Montana": "59001",
            "Nebraska": "68101",
            "Nevada": "89501",
            "New Hampshire": "03101",
            "New Jersey": "07001",
            "New Mexico": "87101",
            "New York": "10001",
            "North Carolina": "27501",
            "North Dakota": "58102",
            "Ohio": "44101",
            "Oklahoma": "73101",
            "Oregon": "97201",
            "Pennsylvania": "19101",
            "Rhode Island": "02901",
            "South Carolina": "29201",
            "South Dakota": "57101",
            "Tennessee": "37201",
            "Texas": "73301",
            "Utah": "84101",
            "Vermont": "05601",
            "Virginia": "23218",
            "Washington": "98101",
            "West Virginia": "25301",
            "Wisconsin": "53201",
            "Wyoming": "82001"
        }
        for state, zipcode in state_zipcodes.items():
            url = f'https://candelamedical.com/patient/find-a-provider/?country=United+States&distance=25&unit=m&address={zipcode}&cf=find&treatment=any&brand=9'
            yield scrapy.Request(url=url, callback=self.parse)




    def parse(self, response):
        try:
            cards = response.xpath('//div[@class="result mb-4"]')

            for card in cards:
                data = {}
                data['provider-name'] = card.xpath('.//h6[@class="px-3 py-2 mb-0 provider-name"]/text()').get()
                data['street'] = card.xpath(
                    './/div[@class="provider-info"]//div[@class="location-address"]/text()').get().replace('\n',
                                                                                                           '').replace(
                    "                                           ", "")

                data['city'] = \
                card.xpath('.//div[@class="provider-info"]//div[@class="location-address"]/text()[2]').get().rsplit(" ",
                                                                                                                    1)[
                    0].replace('\n', '').replace("                                           ", "")
                data['state'] = \
                card.xpath('.//div[@class="provider-info"]//div[@class="location-address"]/text()[2]').get().rsplit(" ",
                                                                                                                    1)[
                    1]
                data['country'] = card.xpath(
                    './/div[@class="provider-info"]//div[@class="location-address"]/text()[3]').get().replace('\n',
                                                                                                              '').replace(
                    "                                           ", "")
                data['number'] = card.xpath('.//div[@class="col-lg-5"]//div[@class="provider-info"][1]/a/text()').get()
                data['website link'] = card.xpath(
                    './/div[@class="col-lg-5"]//div[@class="provider-info"][2]/a/@href').get()
                data['in this location'] = ' '.join(card.xpath(
                    './/div[@class="col-lg-5"]//div[@class="provider-info"][3]//div[@class="location-system"]//text()').extract())
                yield data
        except Exception as e:
            print("Exception occurred", e)


   