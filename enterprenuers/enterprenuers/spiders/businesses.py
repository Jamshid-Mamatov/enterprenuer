import scrapy


class BusinessesSpider(scrapy.Spider):
    name = 'businesses'
    allowed_domains=['entrepreneur.com']
    start_urls=['https://www.entrepreneur.com/franchises/category/personal-care-businesses']

    def parse(self, response):
        products={
            "name":[],
            "description":[],
            "initial investment":[],
            "industry":[],
        }
        for name in response.xpath('//p[@class="text-base font-medium text-gray-700 w-1/2"]/text()').getall():
            if name.strip() != "":
                products['name'].append(name.strip())
           
        
        for description in response.xpath('//p[@class="text-sm font-medium text-gray-700"]/text()').getall():
            products['description'].append(description.strip())
           
        
        for initial_investment in response.xpath('//p[@class="text-sm text-gray-700"]/text()').getall()[:-4]:
            products['initial investment'].append(initial_investment.strip())
        yield products
       
        for link in response.xpath('//a[@class="flex items-center w-full"]/@href'):
    
            yield response.follow(link.get(),callback=self.parse_data)
    
    
    def parse_data(self,response):
        
        yield {
            "industry" :  response.xpath('//a[@class="text-blue-800 hover:underline"]/text()').get(),
            "related categories" : response.xpath('//a[@class="text-blue-800 hover:underline"]/text()').getall()[1:-4],
        }
        
