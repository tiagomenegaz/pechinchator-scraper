import scrapy


class BaseThreadSpider(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def parse(self, response):
        raise NotImplementedError

    def parse_thread_content(self, response):
        raise NotImplementedError
