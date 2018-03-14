# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 用户数据
class JianshuUserItem(scrapy.Item):
    # 用户名
    name = scrapy.Field()
    # 作者标志
    article_s = scrapy.Field()
    # 主页链接地址
    users_url = scrapy.Field()
    # 关注量
    attention = scrapy.Field()
    # 粉丝数
    fans = scrapy.Field()
    # 文章数
    article = scrapy.Field()
    # 字数
    words_num = scrapy.Field()
    # 收获喜欢
    gain_like = scrapy.Field()
    # 收获喜欢
    intro = scrapy.Field()


# 文章数据
class JianshuArticleItem(scrapy.Item):
    # 文章标题
    article_title = scrapy.Field()
    # 作者
    article_autho = scrapy.Field()
    # 图像
    image = scrapy.Field()
    # 作者标志
    article_s = scrapy.Field()
    # 最后编辑时间
    article_edit_time = scrapy.Field()
    # 字数
    article_num = scrapy.Field()
    # 阅读数
    article_read = scrapy.Field()
    # 评论数
    article_comment = scrapy.Field()
    # 喜欢数
    article_like = scrapy.Field()
    # 赞赏数
    article_admire = scrapy.Field()
    # 作者信息：写了 **** 字，被 **** 人关注，获得了 **** 个喜欢
    # article_autho_info = scrapy.Field()
    # 作者签名信息
    article_autho_intro = scrapy.Field()
    # 正文——文本——信息
    article_txt = scrapy.Field()
    # 文章页面链接
    article_url = scrapy.Field()
    # 微博长图链接
    weibo_image = scrapy.Field()


# from scrapy.loader import ItemLoader
# from scrapy.loader.processors import MapCompose, TakeFirst, Join
#
#
# class ExampleLoader(ItemLoader):
#     default_item_class = JianshuUserItem
#     default_input_processor = MapCompose(lambda s: s.strip())
#     default_output_processor = TakeFirst()
#     description_out = Join()
