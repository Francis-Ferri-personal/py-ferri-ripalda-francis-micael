import scrapy

class IntroSCrapy(scrapy.Spider):
    name = "introduccion_spider"
    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url = url)

    def parse(self, response):
        etiqueta_contenedora = response.css(
            'article.product_pod'
        )

        urlsImagen = etiqueta_contenedora.css(
            ".image_container > a > img::attr(src)"
        ).extract()
        print("IMAGENES")
        print(urlsImagen)
        
        starRatings = etiqueta_contenedora.css(
            ".star-rating::attr(class)"
        ).extract()
        stars = list(map(lambda starRating: starRating.split()[1], starRatings))
        print("STARS")
        print(stars)

        titulos = etiqueta_contenedora.css(
            'h3 > a::text'
        ).extract()
        print("TITULOS")
        print(titulos)
        
        prices = etiqueta_contenedora.css(
            ".product_price > .price_color::text"
        ).extract()
        prices = list(map(lambda precio: float(precio[1:]), prices))
        print("PRICE")
        print(prices)
        
        stocks = etiqueta_contenedora.css(
            ".product_price > .instock::text"
        ).extract()
        stocks = list(map(lambda stock: stock.strip(), stocks))
        stocks = list(filter(lambda stock: stock != '', stocks))
        print("STOCKS")
        print(stocks)

        
            
             


# scrapy crawl introduccion_spider