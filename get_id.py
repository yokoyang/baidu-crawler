# coding:utf-8
import requests
import re
from MySqlConn import Mysql

# 申请资源
mysql = Mysql()

for i in range(2):
    page = i * 50
    page_url = "http://tieba.baidu.com/f?kw=%E5%90%8C%E6%B5%8E%E5%A4%A7%E5%AD%A6&ie=utf-8&pn=" + str(page)
    r = requests.get(page_url)
    ret = re.findall(r'(<a href="/p/\d+)', r.text)
    print (len(ret))
    values = list()
    topic = '同济大学'
    for j in ret:
        baidu_id = 'http://tieba.baidu.com'
        baidu_id += j[9:]
        values.append([baidu_id, topic])
    mysql.insertMany('INSERT IGNORE INTO baidu_info(baidu_id,topic) values(%s,%s)', values)

# 释放资源
mysql.dispose()
