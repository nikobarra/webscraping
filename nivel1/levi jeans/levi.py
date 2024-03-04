# Importamos las clases necesarias de Scrapy
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess


# Definimos la clase "Levi" que hereda de "Item" de Scrapy.
# Esta clase representa un producto de la página web de Levi.
# Contiene tres campos: "id", "title" y "price".
class Levi(Item):
    id = Field()
    title = Field()
    price = Field()


# Definimos la clase "LeviSpider" que hereda de "Spider" de Scrapy.
# Esta clase representa el spider que extraerá la información de la página web de Levi.
class LeviSpider(Spider):
    name = "Levi"  # Nombre del spider
    custom_settings = {  # Configuración personalizada del spider
        "USER_AGENT": "Mozilla/5. (Windows NT 0.0;64; x4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.185 Safari/537.36"  # User agent personalizado
    }
    start_urls = [
        "https://www.levi.com/ES/es_ES/ropa/c/levi_clothing"
    ]  # URL inicial del spider

    # Función que se encarga de procesar la respuesta del servidor.
    def parse(self, response):

        # Creamos un objeto "Selector" para extraer información de la respuesta.
        sel = Selector(response)

        # Extraemos todos los elementos que representan productos.
        clothes = sel.xpath('//div[@class="product-cell"]')

        # Iteramos sobre cada producto.
        for i, item in enumerate(clothes):

            # Creamos un objeto "ItemLoader" para cargar la información del producto en un objeto "Levi".
            item = ItemLoader(Levi(), item)

            # Extraemos el título del producto y lo almacenamos en el campo "title" del objeto "Levi".
            item.add_xpath("title", ".//div[@class='product-name']/text()")

            # Extraemos el precio del producto y lo almacenamos en el campo "price" del objeto "Levi".
            item.add_xpath("price", ".//div[@class='product-price']//span/text()")

            # Almacenamos el índice del producto en el campo "id" del objeto "Levi".
            item.add_value("id", i)

            # Devolvemos el objeto "Levi" con la información del producto.
            yield item.load_item()


# Creamos un objeto CrawlerProcess con la configuración deseada
# En este caso, estamos configurando el formato del archivo de salida (csv) y la ruta del archivo (clothes.csv)
process = CrawlerProcess({"FEED_FORMAT": "csv", "FEED_URI": "clothes.csv"})
# Ejecutamos el spider LeviSpider utilizando el objeto CrawlerProcess

process.crawl(LeviSpider)
# Iniciamos el proceso de crawling

process.start()
