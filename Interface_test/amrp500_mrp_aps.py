#参数说明：1.工厂别
#.........2.MRP版本号

import requests
import re
import sys

# 网站获取数据Api
if sys.argv[1] == 'keboda':
    url = "http://172.16.200.144:8100/api/erp/syncMrp/kbd_sh?env=kbdsh&ver=%s" % (sys.argv[2])
if sys.argv[1] == 'zjkbddz':
    url = "http://172.16.200.144:8100/api/erp/syncMrp/kbd_jx?env=kbdjxdz&ver=%s" % (sys.argv[2])
print(url)

# 构建请求
resp = requests.request("get", url)
l_str = resp.text

# 获取APS返回的结果
pattern = ".*(APS_MPS\d{6}_\d{4}).*"   #正则表达式
comp = re.compile(pattern)                #正则模式

result = comp.findall(l_str)              #搜索结果
print(result[0])
