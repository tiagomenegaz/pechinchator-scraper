import multiprocessing

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.blocking import BlockingScheduler

from pechinchator_scraper.spiders.hardmob_spider import HardmobSpider
from pechinchator_scraper.spiders.adrenaline_spider import AdrenalineSpider
from pechinchator_scraper.spiders.promobit_spider import PromobitSpider
from pechinchator_scraper.spiders.kabum_spider import KabumSpider

scheduler = BlockingScheduler()

def kabum_crawl():
    spider_runner = CrawlerProcess(get_project_settings())
    spider_runner.crawl(KabumSpider)
    spider_runner.start()

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


@scheduler.scheduled_job("interval", minutes=3)
def run():
    process = multiprocessing.Process(target=kabum_crawl)
    process.start()

if __name__ == '__main__':
    scheduler.start()
