import scrapy

from pechinchator_scraper.items.thread_item import ThreadItem

ADRENALINE_BASE_URL = "https://adrenaline.uol.com.br/forum/{}"


class AdrenalineSpider(scrapy.Spider):
    name = "adrenaline"
    allowed_domains = ["adrenaline.uol.com.br"]
    start_urls = ["https://adrenaline.uol.com.br/forum/forums/for-sale.221/"]

    def parse(self, response):
        thread_block_selectors = response.css(
            "li.discussionListItem.visible:not(.sticky):not(.locked)"
        )

        for thread_block in thread_block_selectors:
            thread = ThreadItem()
            title_block = thread_block.css("div.titleText")
            stats_block = thread_block.css("div.stats")

            thread_id = thread_block.css("li::attr(id)").extract_first()
            url = ADRENALINE_BASE_URL.format(
                title_block.css("a[title]::attr(href)").extract_first()
            )
            title = title_block.css("a[title]::text").extract_first()
            replies, visits = stats_block.css("div.stats dd::text").extract()

            thread.update({
                "url": url,
                "title": title,
                "replies_count": replies,
                "visits_count": visits,
                "thread_id": thread_id.strip("thread-"),
                "source_id": self.name,
            })

            yield response.follow(
                url,
                callback=self.parse_thread_content,
                meta={"thread": thread}
            )

    def parse_thread_content(self, response):
        thread = response.meta["thread"]
        thread_date_block = response.css("#pageDescription .DateTime")
        thread_date_block = thread_date_block.css(
            "::attr(data-datestring), ::attr(data-timestring)"
        )

        thread["posted_at"] = " ".join(thread_date_block.extract())
        thread["content_html"] = response.css(
            ".messageContent .messageText"
        ).extract_first()

        yield thread
