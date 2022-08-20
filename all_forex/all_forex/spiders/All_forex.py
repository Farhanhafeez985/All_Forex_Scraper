import scrapy
from scrapy import Request


class AllForexSpider(scrapy.Spider):
    name = 'All_forex'

    # allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']
    custom_settings = {'ROBOTSTXT_OBEY': False, 'LOG_LEVEL': 'INFO',
                       'CONCURRENT_REQUESTS_PER_DOMAIN': 5,
                       'RETRY_TIMES': 5,
                       'FEED_URI': 'output.csv',
                       'FEED_FORMAT': 'csv',
                       }

    def start_requests(self):
        url = 'https://allforexbonus.com/forex-broker-reviews/'
        yield Request(url, self.parse)

    def parse(self, response):
        brokers_list = response.xpath(
            "//div[@id='tabal']/div/div[@class='float-left common']/a[text()='Overview']/@href").extract()
        for broker_url in brokers_list:
            yield Request(broker_url, self.parse_detail)

        next_page_url = response.xpath("//link[@rel='next']/@href").get()
        if next_page_url:
            yield Request(next_page_url, self.parse)

    def parse_detail(self, response):
        yield {
            'Broker Name': response.xpath("//h2[@class='main-overview-title']/text()").get().strip().replace('Overview',
                                                                                                             ''),
            'Regulated By': response.xpath("//p[contains(b/text(),'Regulated By')]/b/following-sibling::text()").get(),
            'Headquarters': response.xpath(
                "//p[contains(b/text(),'Headquarters')]/noscript/following-sibling::text()").get(),
            'Mini Deposit': response.xpath("//p[contains(b/text(),'Min Despsit')]/b/following-sibling::text()").get(),
            'US Clients': self.get_boolen_value(response.xpath("//p[contains(b/text(),'US Clients')]/i/@class").get()),
            'Leverage': response.xpath("//p[contains(b/text(),'Leverage')]/b/following-sibling::text()").get(),
            'Established Year': response.xpath(
                "//p[contains(b/text(),'Established Year')]/b/following-sibling::text()").get(),
            'Base Currencies': response.xpath(
                "//td[contains(text(),'Base Currencies')]/following-sibling::td/text()").get(),
            'Type Of Brokers': response.xpath(
                "//td[contains(text(),'Type Of Brokers')]/following-sibling::td/text()").get(),
            'Trading Platform': response.xpath(
                "//td[contains(text(),'Trading Platform')]/following-sibling::td/text()").get(),
            'Website Language': response.xpath(
                "//td[contains(text(),'Website Language')]/following-sibling::td/text()").get(),
            'Mini Account': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Mini Account')]/following-sibling::td/i/@class").get()),

            'VIP Accounts': self.get_boolen_value(
                response.xpath("//td[contains(text(),'VIP Accounts')]/following-sibling::td/i/@class").get()),
            'Segregated Accounts': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Segregated Accounts')]/following-sibling::td/i/@class").get()),
            'Free Demo Accounts': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Free Demo Accounts')]/following-sibling::td/i/@class").get()),
            'Islamic Account': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Islamic Account')]/following-sibling::td/i/@class").get()),

            'Acc Funding Methods': ''.join(response.xpath(
                "//td[contains(text(),'Acc Funding Methods')]/following-sibling::td/text()").extract()),

            'Acc Withdrawal Methods': ''.join(response.xpath(
                "//td[contains(text(),'Acc Withdrawal Methods')]/following-sibling::td/text()").extract()),

            'Telephone No': response.xpath("//td[contains(text(),'Telephone No')]/following-sibling::td/text()").get(),
            'Email': response.xpath("//td[contains(text(),'Email')]/following-sibling::td/text()").get(),

            '24 Hours Support': self.get_boolen_value(
                response.xpath("//td[contains(text(),'24 Hours Support')]/following-sibling::td/i/@class").get()),

            'Support During Weekends': self.get_boolen_value(response.xpath(
                "//td[contains(text(),'Support During Weekends')]/following-sibling::td/i/@class").get()),
            'Address': response.xpath("//td[contains(text(),'Address')]/following-sibling::td/text()").get(),

            'Publicly Traded': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Publicly Traded')]/following-sibling::td/i/@class").get()),
            'Beginners': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Beginners')]/following-sibling::td/i/@class").get()),
            'Day Trading': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Day Trading')]/following-sibling::td/i/@class").get()),
            'Weekly Trading': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Weekly Trading')]/following-sibling::td/i/@class").get()),
            'Professionals': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Professionals')]/following-sibling::td/i/@class").get()),
            'Swing Trading': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Swing Trading')]/following-sibling::td/i/@class").get()),

            'Hedging': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Hedging')]/following-sibling::td/i/@class").get()),
            'News Trading': self.get_boolen_value(
                response.xpath("//td[contains(text(),'News Trading')]/following-sibling::td/i/@class").get()),
            'Scalping': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Scalping')]/following-sibling::td/i/@class").get()),
            'Automated Trading': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Automated Trading')]/following-sibling::td/i/@class").get()),
            'Indices': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Indices')]/following-sibling::td/i/@class").get()),
            'Commodities': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Commodities')]/following-sibling::td/i/@class").get()),
            'Forex instruments': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Forex instruments')]/following-sibling::td/i/@class").get()),
            'CFDs': self.get_boolen_value(
                response.xpath("//td[contains(text(),'CFDs')]/following-sibling::td/i/@class").get()),
            'ETFs': self.get_boolen_value(
                response.xpath("//td[contains(text(),'ETFs')]/following-sibling::td/i/@class").get()),
            'Stocks': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Stocks')]/following-sibling::td/i/@class").get()),
            'Bonds': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Bonds')]/following-sibling::td/i/@class").get()),
            'Cryptocurrencey': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Cryptocurrencey')]/following-sibling::td/i/@class").get()),
            'Trading Signals': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Trading Signals')]/following-sibling::td/i/@class").get()),
            'Educational Service': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Educational Service')]/following-sibling::td/i/@class").get()),
            'Copy/Social Tradings': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Copy/Social Tradings')]/following-sibling::td/i/@class").get()),
            'Minimum Spreads': response.xpath(
                "//td[contains(text(),'Minimum Spreads')]/following-sibling::td/text()").get(),
            'Commission': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Commission')]/following-sibling::td/i/@class").get()),
            'Fixed Spreads': self.get_boolen_value(
                response.xpath("//td[contains(text(),'Fixed Spreads')]/following-sibling::td/i/@class").get()),
        }

    def get_boolen_value(self, class_name):
        if class_name == 'fas fa-times':
            return False
        else:
            return True
