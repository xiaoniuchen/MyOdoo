import json
import requests

#zb网站获取数据Api
url = "http://ip.taobao.com/service/getIpInfo.php?ip=63.223.108.42"

#构建请求
resp = request = requests.request("get",url)

#print(resp.text)
str = resp.text
#print(str)

#将字符转换为字典
d = json.loads(str)

print(d['code'])
