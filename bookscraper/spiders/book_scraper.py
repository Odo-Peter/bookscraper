from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bookscraper.items import BookscraperItem
import csv

class BookScraper(CrawlSpider):
    name = 'book_scraper'
    start_urls = ["http://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(restrict_css=".nav-list > li > ul > li > a"), follow=True),
        Rule(LinkExtractor(restrict_css=".product_pod > h3 > a"), callback="parse_all_books")
    )

    def parse_all_books(self, response):
        book_item = BookscraperItem()

        book_list = []

        book_item["image_url"] = response.urljoin(response.css(".item.active > img::attr(src)").get())

        book_item["title"] = response.css(".col-sm-6.product_main > h1::text").get()
        book_item["price"] = response.css(".price_color::text").get()
        # book_item["upc"] = response.css(".table.table-striped > tr:nth-child(1) > td::text").get()
        book_item["url"] = response.url

        book_list.append(book_item)

        return book_list
