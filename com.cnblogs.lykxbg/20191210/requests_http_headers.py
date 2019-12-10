# encoding:utf-8
import requests
# 请求头
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
# headers={'User-Agent':user_agent}
# r = requests.get('https://www.cnblogs.com/',headers=headers)
# print r.content

# 获取响应码和响应头
r = requests.get('https://www.baidu.com/')
if r.status_code==requests.codes.ok:
    print r.status_code #响应码
    print r.headers #响应头
    print r.headers.get('Content-Type') #推荐方式，获取其中某个字段，若字段不存在则返回None
#     print r.headers['context-type'] #不推荐，若字段不存在则抛异常
else:
    r.raise_for_status() #当响应码为4xx或5xx时，抛异常，为200时，返回None