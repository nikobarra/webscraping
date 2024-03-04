🔵 Herramientas utilizadas
Scrapy es un marco de trabajo de código abierto de bajo nivel para extraer datos de sitios web y almacenarlos en formatos estructurados como JSON o CSV. Scrapy cuenta con las siguientes herramientas para lograr este objetivo:

Item: Representa un objeto que contiene los datos extraídos de una página web.
Field: Representa un campo dentro de un objeto Item.
CrawlSpider: Clase base para spiders que siguen enlaces de una página web a otra.
Rule: Define una regla de extracción de enlaces y/o procesamiento de respuestas.
LinkExtractor: Extrae enlaces de una página web.
ItemLoader: Facilita la carga de datos en un objeto Item.
Selector: Proporciona una forma sencilla de seleccionar nodos y extraer datos de una página web.
🔴 Función cumplida por el script
El script desarrollado en Python utiliza la librería Scrapy para extraer datos de hoteles de la página web de TripAdvisor para Buenos Aires, Argentina. La información extraída incluye:

Nombre del hotel
Puntuación del hotel
Descripción del hotel
Amenities del hotel
El script define una clase Hotel que hereda de Item y define cuatro campos: name, score, description y amenities. Luego, se define una clase TripAdvisor que hereda de CrawlSpider y establece los dominios permitidos, las URLs de inicio y el retraso de descarga. La clase también define una regla de extracción que sigue enlaces que coincidan con el patrón Hotel_Review- y llama a la función parse_hotel para procesar la respuesta.

La función parse_hotel crea un objeto Selector para analizar la respuesta y un objeto ItemLoader para cargar los datos en el objeto Hotel. Luego, se utilizan expresiones XPath para extraer el nombre, la puntuación, la descripción y las amenities del hotel y se cargan en el objeto ItemLoader. Finalmente, se devuelve el objeto ItemLoader cargado.

Para ejecutar el script, se puede utilizar el comando scrapy runspider trip_scrapy.py -o tripito.csv para guardar los datos extraídos en un archivo CSV llamado tripito.csv.
