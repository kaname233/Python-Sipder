# coding=utf8
import requests
import chardet

r = requests.get('http://www.baidu.com')
print 'content-->' + r.content
print 'text-->' + r.text
print 'encoding-->' + r.encoding

# 手动设置编码
# r.encoding = 'utf-8'
# print r.text

# 使用chardet检测编码更加简便
r.encoding = chardet.detect(r.content)['encoding']
print r.text

# 流模式获取响应
r = requests.get('http://www.baidu.com',stream=True)
print r.raw.read(100) # read函数指定读取的字节数