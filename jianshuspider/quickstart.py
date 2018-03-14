# -*- coding:utf-8 -*-
# __author__ = "jake
# __email__ = "jakejie@163.com"
# FileName = *.py
# Version:1.0
# CreateDay:2018/3/14 10:30
# --#--#--#--#--#--#--#--#--#--#--#-- #


from scrapy import cmdline

cmdline.execute("scrapy crawl jianshu".split())
# cmdline.execute("scrapy crawl jianshu --nolog".split())
