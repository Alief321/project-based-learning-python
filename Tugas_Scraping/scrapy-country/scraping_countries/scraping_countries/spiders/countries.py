import scrapy


class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/simple/"]

    def parse(self, response):
        #This function is called whenever the crawler successfully crawls a URL
        #Extracting the content using css selectors
        countries = response.css("div.container div.row div.country")
        for country in countries:
            name = country.css("h3.country-name::text")[1].get().strip()
            capital = country.css("div.country-info span.country-capital::text").get()
            population = country.css("div.country-info span.country-population::text").get()
            area = country.css("div.country-info span.country-area::text").get()
            
            yield {
                "name": name,
                "capital": capital,
                "population": population,
                "area (km^2)": area
            }
