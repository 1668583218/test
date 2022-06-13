# 通过字符去比对每个 unicode 代表的数字
import re

import requests

# 替换对比字典
num_dict = [
    {'code': 'ec05', 'num': '0'},
    {'code': 'e4b0', 'num': '1'},
    {'code': 'f067', 'num': '2'},
    {'code': 'f166', 'num': '3'},
    {'code': 'ea09', 'num': '4'},
    {'code': 'f6e6', 'num': '5'},
    {'code': 'e9e1', 'num': '6'},
    {'code': 'e75a', 'num': '7'},
    {'code': 'edd2', 'num': '8'},
    {'code': 'ea4b', 'num': '9'}
]


# 替换成数字
def change_data(num_dic, data):
    for i in range(len(num_dic)):
        code = num_dic[i]['code']
        if code in data:
            data = data.replace(code, str(num_dic[i]['num']))
    return data


url = 'https://www.maoyan.com/board/1?timeStamp=1654915622613&channelId=40011&index=6&signKey=caaf7289afd9a366c13b0b42a4fbcbe7&sVersion=1&webdriver=false'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    'Cookie': '__mta=252565174.1654911239556.1654917422225.1654917425327.10; uuid_n_v=v1; uuid=8FB510C0E92611EC8A445B788061A84CA0DF45CE84E24736A16BE4359E06D8DC; _csrf=013cf09f7037479071a07481b126853b9a5641417861b9ba39fddfe97972d85a; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1654911239; _lxsdk_cuid=181506582bac8-013b8537d72af8-26021851-fa000-181506582bac8; _lxsdk=8FB510C0E92611EC8A445B788061A84CA0DF45CE84E24736A16BE4359E06D8DC; __mta=252565174.1654911239556.1654915702289.1654917419752.8; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1654917425; _lxsdk_s=181509aa339-23d-5c4-61%7C%7C38'
}
resp = requests.get(url=url, headers=headers).text
print(resp)
# 爬取测试
realtime = re.findall(r'<span class="stonefont">(. *?)</span>', resp)[0]
realtimes = change_data(num_dict, realtime)
title = re.findall(r'<a href=" /films/1212" title="(.*? )" data-act="boarditem-click”.*?</a>', resp)[0]
print('爬取电影︰%s ,实时票房为∶ %s万' % (title, realtimes))
