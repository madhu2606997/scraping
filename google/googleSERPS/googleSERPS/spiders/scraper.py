
import scrapy 
  
class ExtractUrls(scrapy.Spider): 
    name = "extract"
  
    # request function 
    def start_requests(self): 
        urls = ['https://www.google.com/search?q=best+cardiologist+in+kolkata'] 
          
        for url in urls: 
            yield scrapy.Request(url = url, callback = self.parse) 
  
    # Parse function 
    def parse(self, response):
        print(response)
        filename = 'test.txt'
        with open(filename, 'wb') as f:
            f.write(response)
            self.log('saved file %s' % filename)
        


# data = ExtractUrls()

# print(data)