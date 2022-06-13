import hashlib
import json
import time
import random

import requests


# ts 在 js 中是这样的：
# r = "" + (new Date).getTime()
def get_ts():
    ts = int(time.time() * 1000)
    return ts


# bv 在 js 中是这样的：
# n.md5(navigator.appVersion)
def get_bv():
    # 生成bv
    appVersion = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
    m = hashlib.md5()
    m.update(appVersion.encode('utf-8'))
    bv = m.hexdigest()
    return bv


# salt 在 js 中是这样的：
# r + parseInt(10 * Math.random(), 10)
def get_salt(ts):
    # 生成salt
    num = int(random.random() * 10)
    salt = str(ts) + str(num)
    return salt


# sign 在 js 中是这样的：
# n.md5("fanyideskweb" + e + i + "@6f#X3=cCuncYssPsuRUE")
def get_sign(salt):
    # 生成sign
    a = 'fanyideskweb'
    b = '大'
    c = salt
    d = 'Ygy_4c=r#e#4EX^NUGUc5'
    str_data = a + b + str(c) + d
    # md5加密
    m = hashlib.md5()
    m.update(str_data.encode('utf-8'))
    sign = m.hexdigest()
    return sign


def get_form_date():
    ts = get_ts()
    bv = get_bv()
    salt = get_salt(ts)
    sign = get_sign(salt)
    form_data = {
        'i': '大',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': str(salt),
        'sign': sign,
        'lts': str(ts),
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
    }
    # print(form_data)
    return form_data


url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-929494879@10.108.162.135; OUTFOX_SEARCH_USER_ID_NCOO=966442446.8174331; fanyi-ad-id=306808; fanyi-ad-closed=0; ___rl__test__cookies=1654926680955',
    'Referer': 'https://fanyi.youdao.com/',
}
# print(get_form_date())

resp = requests.post(url=url, headers=headers, data=get_form_date())
dict_result = json.loads(resp.content)
print('翻译结果：', dict_result['translateResult'][0][0]['tgt'])
