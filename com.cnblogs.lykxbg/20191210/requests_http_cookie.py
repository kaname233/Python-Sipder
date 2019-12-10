# encoding:utf-8
import requests
user_agent = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
r = requests.get('https://www.cnblogs.com/',headers=headers)
# 遍历出所有Cookie字段的值
for cookie in r.cookie.keys():
    print cookie+':'+r.cookies.get(cookie)

# 自定义cookie并发送
cookies = dict(name='qiye',age='10')
r = requests.get('http://www.baidu.com',headers=headers,cookies=cookies)
print r.text

# session方式处理cookie:
loginUrl = 'http://www.xxxxxx.com/login'
s = requests.Session()
# 首先访问登录界面，作为游客，服务器会先分配一个cookie
r = s.get(loginUrl,allow_redirects=True)
datas = {'name':'qiye','password':'qiye'}
# 向登录连接发送post请求，验证成功后游客权限转为会员权限
r = s.post(loginUrl, datas, allow_redirects=True)
print r.text