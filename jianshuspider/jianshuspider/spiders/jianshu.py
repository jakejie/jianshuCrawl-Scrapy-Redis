# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# 导入item文件
try:
    from jianshuspider.jianshuspider.items import JianshuArticleItem, JianshuUserItem
except:
    from jianshuspider.items import JianshuArticleItem, JianshuUserItem

from scrapy_redis.spiders import RedisSpider


class JianshuSpider(RedisSpider):
    name = 'jianshu'
    allowed_domains = ['www.jianshu.com']
    # host = 'http://www.jianshu.com/'
    redis_key = "jianshu:start_urls"
    # start_urls = ['http://www.jianshu.com/']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # 提取用户信息规则
        Rule(LinkExtractor(allow=r'/users/'), callback='parse_users', follow=True),
        Rule(LinkExtractor(allow=r'/u/'), callback='parse_users', follow=True),
        # 提取文章信息规则
        Rule(LinkExtractor(allow=r'/p/'), callback='parse_article', follow=True),
    )

    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(JianshuSpider, self).__init__(*args, **kwargs)
    #
    # def start_requests(self):
    #     yield Request("http://www.jianshu.com/", callback=self.parse_article)

    def parse_users(self, response):
        item = JianshuUserItem()
        print(response.url)
        # 用户名
        item["name"] = "".join(response.xpath('//div[@class="title"]/a[@class="name"]/text()').extract())
        # 作者标志
        # try:
        #     item["article_s"] = "".join(re.findall(re.compile(r'u/(.*?)\?|users/(.*?)\?'), response.url))
        # except:
        #     item["article_s"] = response.url.split('/')[-1]
        item["article_s"] = item["article_s"].split('?')[0].split('/')[-1]
        # 主页链接地址
        item["users_url"] = response.url
        # 关注量
        item["attention"] = "".join(response.xpath('//div[@class="info"]/ul/li[1]/div/a/p/text()').extract())
        # 粉丝数
        item["fans"] = "".join(response.xpath('//div[@class="info"]/ul/li[2]/div/a/p/text()').extract())
        # 文章数
        item["article"] = "".join(response.xpath('//div[@class="info"]/ul/li[3]/div/a/p/text()').extract())
        # 字数
        item["words_num"] = "".join(response.xpath('//div[@class="info"]/ul/li[4]/div/p/text()').extract())
        # 收获喜欢
        item["gain_like"] = "".join(response.xpath('//div[@class="info"]/ul/li[5]/div/p/text()').extract())
        # 个性简介
        item["intro"] = "".join(response.xpath('//div[@class="description"]/div/text()').extract()) \
            .replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '')
        return item

    def parse_article(self, response):
        items = JianshuArticleItem()
        print(response.url)
        # 文章标题
        items["article_title"] = "".join(response.xpath('//div[@class="article"]/h1/text()').extract())
        # 作者
        items["article_autho"] = "".join(response.xpath('//div[@class="article"]/div[@class="author"]/\
                                               div[@class="info"]/span[1]/a/text()').extract())
        # 图像
        items["image"] = "".join(response.xpath('//div[@class="article"]/div[@class="author"]/\
                                               a/img/@src').extract())
        # 作者标志
        items["article_s"] = "".join(response.xpath('//div[@class="article"]/div[@class="author"]/\
                                           div[@class="info"]/span[1]/a/@href').extract()).split('/')[-1]
        # 最后编辑时间
        items["article_edit_time"] = "".join(response.xpath('//div[@class="article"]/div[@class="author"]/\
                                           div[@class="info"]/div[@class="meta"]/span[1]/text()').extract()) \
            .replace('*', '')
        # 字数
        items["article_num"] = "".join(response.xpath('//div[@class="article"]/div[@class="author"]/\
                                           div[@class="info"]/div[@class="meta"]/span[2]/text()').extract())[3:]
        # 阅读数
        items["article_read"] = "".join(re.findall(re.compile(r'"views_count":([0-9]{1,10}),'), response.text))
        # 评论数
        items["article_comment"] = "".join(re.findall(re.compile(r'"comments_count":([0-9]{1,10}),'), response.text))
        # 喜欢数
        items["article_like"] = "".join(re.findall(re.compile(r'"likes_count":([0-9]{1,10}),'), response.text))
        # 赞赏数
        items["article_admire"] = "".join(
            re.findall(re.compile(r'"total_rewards_count":([0-9]{1,10}),'), response.text))
        # 作者签名信息
        items["article_autho_intro"] = "".join(
            response.xpath('//div[@class="follow-detail"]/div[@class="signature"]/text()').extract())
        # 正文——文本——信息
        items["article_txt"] = "\n".join(response.xpath('//div[@class="show-content"]/div[1]/p/text()|\
                                                //div[@class="show-content"]/div[1]/p/b/text()|\
                                                //div[@class="show-content"]/div[1]/p/a/text()').extract())
        # 文章页面链接
        items["article_url"] = response.url.split('?')[0]
        # 微博长图链接
        items["weibo_image"] = "".join(response.xpath('//div[@class="share-group"]/a[3]/@href').extract())

        return items

    # def parse_item(self, response):
    #     i = {}
    #     # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
    #     # i['name'] = response.xpath('//div[@id="name"]').extract()
    #     # i['description'] = response.xpath('//div[@id="description"]').extract()
    #     return i
