#encoding=utf8

import requests
import bs4
import chardet
response = requests.get("http://finance.sina.com.cn/")
result = bs4.BeautifulSoup(response.content, "lxml")

print result.title.string