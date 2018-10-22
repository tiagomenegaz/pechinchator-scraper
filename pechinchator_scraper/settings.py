# -*- coding: utf-8 -*-
from dotenv import load_dotenv

load_dotenv()

BOT_NAME = 'pechinchator_scraper'

SPIDER_MODULES = ['pechinchator_scraper.spiders']
NEWSPIDER_MODULE = 'pechinchator_scraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure a delay for requests for the same website
DOWNLOAD_DELAY = 5

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
}

# Enable and configure HTTP caching
HTTPCACHE_ENABLED = True
