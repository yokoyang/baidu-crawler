# coding:utf-8
import requests
import re
from MySqlConn import Mysql
import json, urllib
from urllib import urlencode

global pic_id
pic_id = 15


def getJsonContent(res):
    url_list = list()
    url_list.append(res['cover'])
    rec_list = res['video_rec']

    for i in range(len(rec_list)):
        url_list.append((rec_list[i])['cover'])
    return url_list


def main():
    # 配置您申请的APPKey
    appkey = "****************"
    f = open("name.txt")  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    nameList = list()
    while line:
        nameList.append(line.strip('\n'))
        line = f.readline()
    f.close()

    for i in range(70, 75):
        movieName = nameList[i]
        # 申请资源
        # 1.影视搜索
        request1(appkey, movieName, "GET")
        # 释放资源


# 影视搜索
def request1(appkey, movieName, m="GET"):
    values = list()

    url = "http://op.juhe.cn/onebox/movie/video"
    params = {
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "json",  # 返回数据的格式,xml或json，默认json
        "q": movieName,  # 影视搜索名称
    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            mysql = Mysql()
            url_list = getJsonContent((res["result"]))
            # print((res["result"])['cover'])
            for i in range(len(url_list)):
                global pic_id
                values.append([pic_id, url_list[i]])
                pic_id += 1
            mysql.insertMany('INSERT IGNORE INTO picture(picture_id,picture_url) values(%s,%s)', values)
            mysql.dispose()
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")


if __name__ == '__main__':
    main()


    # # 申请资源
    # mysql = Mysql()
    #
    # # for i in range(2):
    # values =[2,'http://p3.qhimg.com/t017ba04f96c6d97587.jpg']
    # mysql.insertMany('INSERT IGNORE INTO picture(picture_id,picture_url) values(%s,%s)', values)
    #
    # # 释放资源
    # mysql.dispose()
