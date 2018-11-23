import multiprocessing

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.blocking import BlockingScheduler

from pechinchator_scraper.spiders.hardmob_spider import HardmobSpider
from pechinchator_scraper.spiders.adrenaline_spider import AdrenalineSpider
from pechinchator_scraper.spiders.promobit_spider import PromobitSpider

scheduler = BlockingScheduler()


def crawl():
    spider_runner = CrawlerProcess(get_project_settings())
    spider_runner.crawl(HardmobSpider)
    spider_runner.crawl(AdrenalineSpider)
    spider_runner.crawl(PromobitSpider)
    spider_runner.start()


@scheduler.scheduled_job("interval", minutes=5)
def run():
    process = multiprocessing.Process(target=crawl)
    process.start()


if __name__ == '__main__':
    scheduler.start()
