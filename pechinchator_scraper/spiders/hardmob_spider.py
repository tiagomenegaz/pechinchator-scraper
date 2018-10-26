import scrapy
import re

from pechinchator_scraper.items.thread_item import ThreadItem

THREAD_VISITS_REGEX_PATTERN = r"\d+.*"


class HardmobSpider(scrapy.Spider):
    name = "hardmob"
    allowed_domains = ["www.hardmob.com.br"]
    start_urls = ["http://www.hardmob.com.br/promocoes/"]

    def parse(self, response):
        thread_block_selectors = response.css("ol#threads > .threadbit")

        for thread_block in thread_block_selectors:
            thread = ThreadItem()
            thread_id = thread_block.css("li::attr(id)").extract_first()
            url = thread_block.css("a.title::attr(href)").extract_first()
            title = thread_block.css("a.title::text").extract_first()
            posted_at = None

            stats_block = thread_block.css("ul.threadstats > li:not(.hidden)")

            replies = stats_block.css(".understate::text").extract_first()
            visits = stats_block.css("li:not(.hidden)::text").extract()[1]
            visits = re.search(THREAD_VISITS_REGEX_PATTERN, visits).group()

            thread.update({
                "url": url,
                "title": title,
                "posted_at": posted_at,
                "replies_count": replies,
                "visits_count": visits,
                "thread_id": thread_id.strip("thread_"),
                "source_id": self.name,
            })

            yield response.follow(
                url,
                callback=self.parse_thread_content,
                meta={"thread": thread}
            )

    def parse_thread_content(self, response):
        thread = response.meta["thread"]

        details_block = response.css(".postdetails")
        thread["content_html"] = details_block.css(".content").extract_first()
        thread["posted_at"] = " ".join([
            response.css(".date::text").extract_first().strip(),
            response.css(".date > .time::text").extract_first(),
        ])

        yield thread
