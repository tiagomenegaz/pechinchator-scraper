import scrapy


class BaseThreadSpider(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start_requests(self):
        for url in self.start_urls:
            meta = {"dont_cache": True}
            yield scrapy.Request(url=url, callback=self.parse, meta=meta)

    def parse(self, response):
        raise NotImplementedError

    def parse_thread_content(self, response):
        raise NotImplementedError
