# Scrapy settings for ckk project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#######################################################################
# Scrapy Project settings
BOT_NAME = 'ckk'
SPIDER_MODULES = ['ckk.spiders']
NEWSPIDER_MODULE = 'ckk.spiders'
ROBOTSTXT_OBEY = True
# USER_AGENT = '  "Googlebot/2.1 (+http://www.google.com/bot.html)"'
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}
# AUTOUNIT_ENABLED = True
# DOWNLOADER_MIDDLEWARES = {
#    'crawler.middlewares.CrawlerDownloaderMiddleware': 543,
# }
ITEM_PIPELINES = {
  'ckk.pipelines.ValidationPipeline': 400,
}

AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False
HTTPCACHE_ENABLED = True
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_IGNORE_HTTP_CODES = []
# DOWNLOAD_DELAY = 3
