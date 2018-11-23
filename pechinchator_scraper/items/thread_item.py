import scrapy


class ThreadItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    posted_at = scrapy.Field()
    content_html = scrapy.Field()
    replies_count = scrapy.Field()
    visits_count = scrapy.Field()
    thread_id = scrapy.Field()
    source_id = scrapy.Field()
    offer_url = scrapy.Field()

    @property
    def id(self):
        return "-".join([self.get("thread_id"), self.get("source_id")])
