# coding=utf8
import requests
# Get请求
r = requests.get('http://www.baidu.com')
print r.content

# Post请求
postdata = {'key':'value'}
r = requests.post('http://www.xxxxxxxx.com/login',data=postdata)
print r.content

#带参的Get请求
# 方式一：
r = requests.get('http://zzk.cnblogs.com/s/blogpost?Keywords=python&pageindex=1')
# 方式二：
payload = {'Keywords':'python','pageindex':1}
r = requests.get('http://zzk.cnblogs.com/s/blogpost',params=payload)
print r.url
print r.content