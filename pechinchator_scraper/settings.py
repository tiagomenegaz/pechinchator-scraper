# -*- coding: utf-8 -*-
from dotenv import load_dotenv
import os

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

# DB Settings

MONGODB_SERVER = os.getenv("MONGODB_SERVER", "127.0.0.1")
MONGODB_PORT = int(os.getenv("MONGODB_PORT", 27017))
MONGODB_DB = os.getenv("MONGODB_DB")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION")
