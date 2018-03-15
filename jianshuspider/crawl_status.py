# -*- coding:utf-8 -*-
# __author__ = "jake
# __email__ = "jakejie@163.com"
# FileName = *.py
# Version:1.0
# CreateDay:2018/3/15 16:01
# --#--#--#--#--#--#--#--#--#--#--#-- #

import requests
import json

baseUrl = 'http://127.0.0.1:6800/'
daemUrl = 'http://127.0.0.1:6800/daemonstatus.json'
listproUrl = 'http://127.0.0.1:6800/listprojects.json'
listspdUrl = 'http://127.0.0.1:6800/listspiders.json?project=%s'
listspdvUrl = 'http://127.0.0.1:6800/listversions.json?project=%s'
listjobUrl = 'http://127.0.0.1:6800/listjobs.json?project=%s'
delspdvUrl = 'http://127.0.0.1:6800/delversion.json'

# http://127.0.0.1:6800/daemonstatus.json
# 查看scrapyd服务器运行状态
r = requests.get(daemUrl)
print('1.stats :\n %s \n\n' % r.text)
# http://127.0.0.1:6800/listprojects.json
# 获取scrapyd服务器上已经发布的工程列表
r = requests.get(listproUrl)
print('1.1.listprojects : [%s]\n\n' % r.text)

"""

if len(json.loads(r.text)["projects"]) > 0:
    project = json.loads(r.text)["projects"][0]

# http://127.0.0.1:6800/listspiders.json?project=myproject
# 获取scrapyd服务器上名为myproject的工程下的爬虫清单
listspd = listspd % project
r = requests.get(listspdUrl)
print(
    '2.listspiders : [%s]\n\n' % r.text)
if json.loads(r.text).has_key("spiders") > 0:
    spider = json.loads(r.text)["spiders"][0]

# http://127.0.0.1:6800/listversions.json?project=myproject
##获取scrapyd服务器上名为myproject的工程下的各爬虫的版本
listspdvUrl = listspdvUrl % project
r = requests.get(listspdvUrl)
print(
    '3.listversions : [%s]\n\n' % rtext)
if len(json.loads(r.text)["versions"]) > 0:
    version = json.loads(r.text)["versions"][0]

# http://127.0.0.1:6800/listjobs.json?project=myproject
# 获取scrapyd服务器上的所有任务清单，包括已结束，正在运行的，准备启动的。
listjobUrl = listjobUrl % proName
r = requests.get(listjobUrl)
print(
    '4.listjobs : [%s]\n\n' % r.text)

# schedule.json
# http://127.0.0.1:6800/schedule.json -d project=myproject -d spider=myspider
# 启动scrapyd服务器上myproject工程下的myspider爬虫，使myspider立刻开始运行，注意必须以post方式
schUrl = baseurl + 'schedule.json'
dictdata = {"project": project, "spider": spider}
r = reqeusts.post(schUrl, json=dictdata)
print(
    '5.1.delversion : [%s]\n\n' % r.text)

# http://127.0.0.1:6800/delversion.json -d project=myproject -d version=r99'
# 删除scrapyd服务器上myproject的工程下的版本名为version的爬虫，注意必须以post方式
delverUrl = baseurl + 'delversion.json'
dictdata = {"project": project, "version": version}
r = reqeusts.post(delverUrl, json=dictdata)
print(
    '6.1.delversion : [%s]\n\n' % r.text))

# http://127.0.0.1:6800/delproject.json -d project=myproject
# 删除scrapyd服务器上myproject工程，注意该命令会自动删除该工程下所有的spider，注意必须以post方式
delProUrl = baseurl + 'delproject.json'
dictdata = {"project": project}
r = reqeusts.post(delverUrl, json=dictdata)
print('6.2.delproject : [%s]\n\n' % r.text)
"""