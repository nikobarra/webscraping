# 👖 Scraper de Levi 👖

Este repositorio contiene un scraper de la página web de Levi que extrae información sobre los productos disponibles en la sección de ropa. El scraper está implementado en Python utilizando la biblioteca Scrapy.

## 🛍️ Herramientas utilizadas 🛍️

-   Scrapy: biblioteca de Python para realizar web scraping.
-   Selector: utilidad de Scrapy para extraer información de las respuestas del servidor.
-   ItemLoader: utilidad de Scrapy para cargar la información extraída en objetos de tipo "Item".

## 🔍 Funcionamiento del scraper 🔍

1. El scraper accede a la URL inicial de la página web de Levi: `https://www.levi.com/ES/es_ES/ropa/c/levi_clothing`.
2. Utilizando la clase `Selector`, el scraper extrae todos los elementos que representan productos.
3. El scraper itera sobre cada producto y utiliza la clase `ItemLoader` para cargar la información del producto en un objeto de tipo `Levi`.
4. La información del producto se extrae utilizando las expresiones XPath adecuadas.
5. El objeto `Levi` con la información del producto se devuelve al scraper.

## 🚀 Ejecución del scraper 🚀

Para ejecutar el scraper, se debe ejecutar el siguiente comando en la terminal:

```bash
scrapy runspider levi.py -o clothes.csv
```
