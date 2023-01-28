# plan

## find tables
- name : response.xpath('//p[@class="text-base font-medium text-gray-700 w-1/2"]/text()').getall()
- description: response.xpath('//p[@class="text-sm font-medium text-gray-700"]/text()').getall()
- initial investment: response.xpath('//p[@class="text-sm text-gray-700"]/text()').getall()
- link :  response.xpath('//a[@class="flex items-center w-full"]/@href').getall()
- industry : response.xpath('//a[@class="text-blue-800 hover:underline"]/text()').get()
- related categories : response.xpath('//a[@class="text-blue-800 hover:underline"]/text()').getall()[1:-4]
- founded : response.xpath('//dd[@class="mt-1 text-base text-gray-900 font-normal sm:mt-0 sm:col-span-2"]/text()').getall() [6]
- parent company : 7
- leadership : 8 
- corporate address: 9 
