# 百度贴吧爬虫 version 1.0 
## get_id.py
根据主题，获取到主题相关的所有贴子

## crawler.py
根据贴子url，爬取贴子下面的所有内容

## DB配置
schemas:crawler
tabel:baidu_info

### 表项:
- baidu_id varchar 512
- topic varchar 1024
