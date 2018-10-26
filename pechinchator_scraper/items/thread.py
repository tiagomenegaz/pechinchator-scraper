import scrapy


class Thread(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    posted_at = scrapy.Field()
    content_html = scrapy.Field()
    replies_count = scrapy.Field()
    visits_count = scrapy.Field()
    thread_id = scrapy.Field()
    source_id = scrapy.Field()
