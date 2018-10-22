import scrapy


class Thread(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    posted_at = scrapy.Field()
    replies_count = scrapy.Field()
    visits_count = scrapy.Field()
