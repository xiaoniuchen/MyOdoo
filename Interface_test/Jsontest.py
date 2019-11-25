#by 侯禹江
#2018、/0/27
import json
from urllib.request import Request, urlopen

#zb网站获取数据Api
url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=15821383602"
#包装头部
firefox_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
#构建请求
request = Request( url, headers=firefox_headers )
html = urlopen( request )
#获取数据
data = html.read()
#转换成字符串
strs = str(data)
#截取字符串
print(strs)
# strs_for_json = strs[44:]
# strs_for_json= strs_for_json[:-2]
#print(strs_for_json)