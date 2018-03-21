# -*- coding: utf-8 -*-
import random
from .useragent import user_agents

BOT_NAME = 'jianshuspider'

SPIDER_MODULES = ['jianshuspider.spiders']
NEWSPIDER_MODULE = 'jianshuspider.spiders'

REDIRECT_ENABLED = True
RETRY_TIMES = 100
DOWNLOAD_TIMEOUT = 10  # 下载超时时间


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:


DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    # "Connection": "keep-alive",
    "User-Agent": random.choice(user_agents),
    "Host": "www.jianshu.com",
}
ITEM_PIPELINES = {
    'jianshuspider.pipelines.JianshuspiderPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400
}
# ------------------Redis分布式配置---------------------------------------------
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379  # 6379
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 不清除Redis队列、这样可以暂停/恢复 爬取
SCHEDULER_PERSIST = True

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'jianshuspider.middlewares.JianshuspiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'jianshuspider.middlewares.JianshuspiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     'jianshuspider.pipelines.JianshuspiderPipeline': 300,
#     'scrapy_redis.pipelines.RedisPipeline': 400
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# # ------------------Redis分布式配置---------------------------------------------
# REDIS_HOST = '*****'
# REDIS_PORT = 6379  # 6379
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"


# 启用Redis调度存储请求队列
# SCHEDULER = "jianshuspider.scrapy_redis.scheduler.Scheduler"

# 确保所有的爬虫通过Redis去重
# DUPEFILTER_CLASS = "jianshuspider.scrapy_redis.dupefilter.RFPDupeFilter"
# SCHEDULER_QUEUE_CLASS = 'jianshuspider.scrapy_redis.queue.SpiderPriorityQueue'

# 默认请求序列化使用的是pickle 但是我们可以更改为其他类似的。PS：这玩意儿2.X的可以用。3.X的不能用
# SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"

# 不清除Redis队列、这样可以暂停/恢复 爬取
# SCHEDULER_PERSIST = True

# 使用优先级调度请求队列 （默认使用）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
# 可选用的其它队列
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'

# 最大空闲时间防止分布式爬虫因为等待而关闭
# 这只有当上面设置的队列类是SpiderQueue或SpiderStack时才有效
# 并且当您的蜘蛛首次启动时，也可能会阻止同一时间启动（由于队列为空）
# SCHEDULER_IDLE_BEFORE_CLOSE = 10

# 将清除的项目在redis进行处理
"""
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300
}
"""
# 序列化项目管道作为redis Key存储
# REDIS_ITEMS_KEY = '%(spider)s:items'

# 默认使用ScrapyJSONEncoder进行项目序列化
# You can use any importable path to a callable object.
# REDIS_ITEMS_SERIALIZER = 'json.dumps'

# 指定连接到redis时使用的端口和地址（可选）
# REDIS_HOST = 'localhost'
# REDIS_PORT = 6379
# 种子队列的信息
# REDIS_URL = None
# REDIS_HOST = '127.0.0.1'
# REDIS_HOST = '*******'
# REDIS_PORT = 6379  # 6379
# FILTER_URL = None
# FILTER_HOST = '127.0.0.1'
# FILTER_HOST = '*************'
# FILTER_PORT = 6379  # 6379
# FILTER_DB = 0
# 指定用于连接redis的URL（可选）
# 如果设置此项，则此项优先级高于设置的REDIS_HOST 和 REDIS_PORT
# REDIS_URL = 'redis://user:pass@hostname:9001'

# 自定义的redis参数（连接超时之类的）
# REDIS_PARAMS  = {}

# 自定义redis客户端类
# REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient'

# 如果为True，则使用redis的'spop'进行操作。
# 如果需要避免起始网址列表出现重复，这个选项非常有用。开启此选项urls必须通过sadd添加，否则会出现类型错误。
# REDIS_START_URLS_AS_SET = False

# RedisSpider和RedisCrawlSpider默认 start_usls 键
# REDIS_START_URLS_KEY = '%(name)s:start_urls'

# 设置redis使用utf-8之外的编码
# REDIS_ENCODING = 'latin1'

# ---------------------------------------------------------------------------------------------
