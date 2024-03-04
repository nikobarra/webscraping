from scrapy.item import Field  # Importando Field desde scrapy.item
from scrapy.item import Item  # Importando Item desde scrapy.item
from scrapy.spiders import (
    CrawlSpider,
    Rule,
)  # Importando CrawlSpider y Rule desde scrapy.spiders
from scrapy.selector import Selector  # Importando Selector desde scrapy.selector
from scrapy.loader.processors import (
    MapCompose,
)  # Importando MapCompose desde scrapy.loader.processors
from scrapy.linkextractors import (
    LinkExtractor,
)  # Importando LinkExtractor desde scrapy.linkextractors
from scrapy.loader import ItemLoader  # Importando ItemLoader desde scrapy.loader


class Hotel(Item):  # Definiendo una clase Hotel que hereda de Item
    name = Field()  # Agregando un campo 'name' de tipo Field
    score = Field()  # Agregando un campo 'score' de tipo Field
    description = Field()  # Agregando un campo 'description' de tipo Field
    amenities = Field()  # Agregando un campo 'amenities' de tipo Field


class TripAdvisor(
    CrawlSpider
):  # Definiendo una clase TripAdvisor que hereda de CrawlSpider
    name = "Hotels"  # Asignando un nombre a la clase
    custom_settings = {  # Configurando settings personalizados
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    allowed_domains = ["tripadvisor.com.ar"]  # Definiendo los dominios permitidos
    start_urls = [  # Definiendo las URLs de inicio
        "https://www.tripadvisor.com.ar/Hotels-g312741-Buenos_Aires_Capital_Federal_District-Hotels.html"
    ]
    download_delay = 2  # Definiendo el retraso de descarga

    rules = (  # Definiendo las reglas de extracción
        Rule(  # Regla 1
            LinkExtractor(
                allow=r"Hotel_Review-"
            ),  # Extraer enlaces que coincidan con el patrón "Hotel\_Review-"
            follow=True,  # Seguir los enlaces extraídos
            callback="parse_hotel",  # Llamar a la función 'parse_hotel' para procesar la respuesta
        ),
    )

    def parse_hotel(
        self, response
    ):  # Definiendo la función 'parse_hotel' para procesar la respuesta
        sel = Selector(
            response
        )  # Creando un objeto Selector para analizar la respuesta
        item = ItemLoader(
            Hotel(), sel
        )  # Creando un objeto ItemLoader para cargar los datos en el objeto Hotel
        item.add_xpath(
            "name", "//h1[@id='HEADING']/text()"
        )  # Agregando el nombre del hotel usando xpath
        score_value = response.xpath(  # Agregando la puntuación del hotel usando xpath
            '//div[contains(@class, "jVDab")]/span/text()[1]'
        ).extract_first()
        item.add_xpath(
            "score", score_value
        )  # Agregando la puntuación del hotel al objeto ItemLoader
        item.add_xpath(  # Agregando la descripción del hotel usando xpath
            "description",
            "//div[@class='fIrGe _T']/text()",
            MapCompose(
                lambda i: i.replace("\n", "").replace("\r", "")
            ),  # Limpiando los saltos de línea y los caracteres de retorno de carro
        )
        item.add_xpath(  # Agregando las amenities del hotel usando xpath
            "amenities", '//div[contains(@data-test-target, "amenity_text")]/text()'
        )
        yield item.load_item()  # Devolviendo el objeto ItemLoader cargado


# scrapy runspider trip_scrapy.py -o tripito.csv
