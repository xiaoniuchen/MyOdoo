import json
import requests
import re

#zb网站获取数据Api
url = "http://172.16.200.144:8100/api/erp/syncMrp/kbd_sh?env=kbdsh&ver=cpf150214"

#构建请求
resp = requests.request("get",url)

l_str = resp.text
# l_str = "<?xml version='1.0'?><message><result>true</result><code>200</code><message>" \
#         "计算任务创建成功，系统很快即可完成！</message><content><scenario_id>995</scenario_id>" \
#         "<scenario_uuid>2fdf23fe-0c3b-11ea-bc9a-0242c0a80003</scenario_uuid><scenario_nr>" \
#         "APS_MPS191121_0009</scenario_nr></content></message>"
#print(l_str)

pattern = ".*(APS_MPS\d{6}_\d{4}).*"
re.compile(pattern)

result = re.findall(pattern,l_str)
print(result[0])
#将字符转换为字典
# d = json.loads(str)
#
# print(d['code'])