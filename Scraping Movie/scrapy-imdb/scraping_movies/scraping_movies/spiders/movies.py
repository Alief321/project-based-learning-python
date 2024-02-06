import scrapy

class MoviesSpider(scrapy.Spider):
    name = "movies"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/"]
    def parse(self, response):
        #This function is called whenever the crawler successfully crawls a URL
        #Extracting the content using css selectors
        movies = response.css("ul li.ipc-metadata-list-summary-item")
        for movie in movies:
            judul = movie.css("a.ipc-title-link-wrapper h3::text").get()
            tahun = movie.css("div.cli-title-metadata span::text")[0].get()
            durasi = movie.css("div.cli-title-metadata span::text")[1].get()
            rating = movie.css("span.ipc-rating-star::attr(aria-label)").get().strip('IMDb rating: ')
            poster = movie.css("img.ipc-image::attr(src)").get()
            #yield or give the scraped info to scrapy
            yield {
            'judul': judul,
            'tahun': tahun,
            'durasi': durasi,
            'rating': rating,
            'poster': poster
            }