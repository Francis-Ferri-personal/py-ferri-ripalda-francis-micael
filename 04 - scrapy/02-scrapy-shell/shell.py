#Scrapy bench nos ayuda a saber  que caracteristicas contiene nuestro compuutador (caracteristicas de performance)
 -->
""" scrapy view https://www.ecuavisa.com/
Para activar la sheel utiliza el siguiente comando: scrapy shell url """
type(response.css('div'))
response.css('title').extract()
response.css('title::text').extract()
len(response.css('.tags .tag::text').extract())
len(response.css('div.tags > a.tag::text').extract())
response.css('.row > div > div:nth-child(2) > .text::text').extract()
response.css('.row > div > div:nth-child(2) > .text::text').extract()


# XPATH
# le damos click derecho y ponemos copy xpath
# Existen casos donde es mucho mas simple utilizar xpatth y existen otros con los que es mucho mas facil usar el css
# para sacar el texto usando xpantg se debe poner al final "/text()"
response.xpath('/html/head/title/text()').extract()
# La nomencaltura de // busca todas las ocurrencias de la etiqueta
response.xpath("//div[@class='tags']/a[@class='tag']/text()").extract()
response.xpath("//title/text()").extract()
response.xpath("//small[@class='author']/text()").extract()
response.xpath("//span[@class='text']/text()").extract()
response.css("a::attr(href)").extract()
response.css("div.quote > span > a::attr(href)").extract()
response.xpath("//div[@class='quote']/span/a/@href").extract()
