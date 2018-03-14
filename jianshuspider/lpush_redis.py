# -*- coding:utf-8 -*-
# __author__ = "jake
# __email__ = "jakejie@163.com"
# FileName = *.py
# Version:1.0
# CreateDay:2018/3/14 15:59
# --#--#--#--#--#--#--#--#--#--#--#-- #

import redis

try:
    r = redis.Redis(host='116.62.64.42', port=6379)
    r.lpush('jianshu:start_urls', 'http://www.jianshu.com')
    print("压入url成功!")
except Exception:
    print("压入失败")
