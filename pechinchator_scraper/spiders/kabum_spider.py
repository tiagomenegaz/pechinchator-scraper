import re
import json
from pechinchator_scraper.items.thread_item import ThreadItem
from pechinchator_scraper.spiders.base_thread_spider import BaseThreadSpider

THREAD_VISITS_REGEX_PATTERN = r"\d+.*"

class KabumSpider(BaseThreadSpider):
    name = "kabum"
    allowed_domains = ["https://cybermonday.kabum.com.br"]
    start_urls = ["https://cybermonday.kabum.com.br/data.json?campanha=cybermonday"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def parse(self, response):
        json_response = response.body_as_unicode()
        products_json = json.loads(json_response)["produtos"]
        filtered_products = [ product for product in products_json.values() if product["quantidade"] > 0 ]

        for product in filtered_products:
            thread = ThreadItem()
            thread["thread_id"] = product["codigo"]
            thread["url"] = "https://www.kabum.com.br/produto/{}".format(product["codigo"])
            price = "R$ " + str(product["vlr_oferta"])
            thread["title"] = product["produto"] + " " + price
            thread["quantity"] = product["quantidade"]
            thread["posted_at"] = "2018-11-26 00:00:00"
            thread["content_html"] = "<span></span>"
            thread["source_id"] = "kabum"
            thread["replies_count"] = 0
            thread["visits_count"] = 0
            yield(thread)
