import scrapy
from scrapy.http import Request
from brreg_scraper.items import BrregScraperItem
from scrapy.loader import ItemLoader


class CompanyInfoSpider(scrapy.Spider):
    name = 'company_info'
    allowed_domains = ['www.brreg.no', 'w2.brreg.no']
    start_urls = ['https://www.brreg.no']
    #start_urls = ['https://w2.brreg.no/enhet/sok/detalj.jsp?orgnr=990598835']
    #url = f'https://w2.brreg.no/enhet/sok/detalj.jsp?orgnr=990598835'
    
    def parse(self, response):

        vat_numbers = ['990598835', '936972403', '920278116', '990598835']
        
        for vat_number in vat_numbers:
            
            yield scrapy.FormRequest.from_response(
                response,
                formname='foretak',
                formdata={'inputparam': vat_number} , 
                callback=self.parse_data)         
    
    def parse_data(self, response):
        l = ItemLoader(item=BrregScraperItem(), selector=response)
        
        l.add_xpath('name', '//div[@id="pagecontent"]/div[3]/div[2]/p')
        l.add_xpath('vat_number', '//*[@id="pagecontent"]/div[2]/div[2]/p')
        l.add_xpath('address', '//div[@id="pagecontent"]/div[5]/div[2]/p')
        l.add_xpath('municipality', '//*[@id="pagecontent"]/div[6]/div[2]/p')
        l.add_xpath('postal_address', '//*[@id="pagecontent"]/div[7]/div[2]/p')
        
        yield l.load_item()
        


# NOTES
     # get() --> get the first element that matches the selection (css or xpath)
     # getall() --> get all elements that match the selection
     
     # XPATH SELECTORS
        # add 'text() to the end of the xpath'
        # url: './/a[@class="p_box_title"]/@href'
            # response.urljoin(product.xpath('.//a[@class="p_box_title"]/@href').get()),
    
    # CSS SELECTORS 
        # ADD '::text' at the end to get just the text
        # links example: products.css('a.product-item-link').attrib['href]