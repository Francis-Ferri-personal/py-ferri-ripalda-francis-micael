import scrapy

class IntroSCrapy(scrapy.Spider):
    name = "fybeca_spider"
    urls = [
        'http://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=150Ypp=25'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url = url)

    def parse(self, response):
        etiqueta_contenedora = response.css(
            'div.price-member'
        )

        precios = etiqueta_contenedora.css(
            ".price::attr(data-bind)"
        ).extract()
        print("PRECIOS")
        print(precios)


