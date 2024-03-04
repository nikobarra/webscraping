Scraper de Hoteles en TripAdvisor
En este repositorio, encontrarás un scraper desarrollado en Python utilizando la librería Scrapy, el cual se encarga de obtener información de hoteles en la página de TripAdvisor para la ciudad de Buenos Aires.

🛠 Herramientas utilizadas
Scrapy: Framework para desarrollar arañas web.
Python: Lenguaje de programación utilizado para el desarrollo del scraper.
💻 Funcionamiento del scraper
El scraper está compuesto por dos clases principales: Hotel y TripAdvisor. La clase Hotel define el esquema de datos a obtener de cada hotel, mientras que la clase TripAdvisor hereda de CrawlSpider y define el comportamiento de la araña web.

La araña web comienza extrayendo los datos de la página principal de hoteles en TripAdvisor para Buenos Aires y, a continuación, sigue los enlaces a las páginas individuales de cada hotel. Para cada hotel, se obtienen los siguientes datos:

Nombre
Puntuación
Descripción
Amenities
Los datos se almacenan en un archivo CSV utilizando el módulo csv de Python.

🚀 Ejecución del scraper
Para ejecutar el scraper, sigue los siguientes pasos:

Asegúrate de tener Python y Scrapy instalados en tu sistema.
Clona este repositorio en tu máquina local.
Ejecuta el siguiente comando en la terminal para instalar las dependencias del proyecto:
bash
Copy code
pip install -r requirements.txt
Ejecuta el scraper con el siguiente comando:
bash
Copy code
scrapy runspider trip_scrapy.py -o tripito.csv
Una vez ejecutado el comando, el scraper generará un archivo CSV llamado tripito.csv con los datos obtenidos de los hoteles en TripAdvisor.

¡Listo! Ahora puedes utilizar los datos obtenidos para tus propios propósitos.
