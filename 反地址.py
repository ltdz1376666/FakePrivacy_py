import time
import requests
import json
from id_validator import validator
import re
import constant


url = "https://account-api.54traveler.com/user/account/update"

headers = {
    "Host": "account-api.54traveler.com",
    "Connection": "keep-alive",
    "charset": "utf-8",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3617 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.188 Mobile Safari/537.36 XWEB/1260117 MMWEBSDK/20240501 MMWEBID/5029 MicroMessenger/8.0.50.2701(0x2800323E) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "platform": "USER_WECHAT_APPLET",
    "authorization": "Basic userToken-367dfbdc-1e5b-495b-8dcd-9631ef8c65cd",
    "content-type": "application/json",
    "user-token": "userToken-367dfbdc-1e5b-495b-8dcd-9631ef8c65cd",
    "Referer": "https://servicewechat.com/wxb1e07e66bd1e2872/630/page-frame.html"
}


data = {
    "id": 613519,
    "email": "",
    "realname": "realname",
    "sex": "女",
    "birthday": "1997-05-14",
    "accountId": 516033,
    "identityType": "MAINLAND_ID_CARD",
    "identityNumber": "identityNumber",
    "isOneself": True,
    "avatar": "https://dao-asset.54traveler.com/travel/example/user.png"
}

def error():
    print('你输入的姓名/身份证可能有误')


# 将字典转换为JSON格式的字符串
json_data = json.dumps(data)
response = requests.put(url, headers=headers, data=json_data)

while True:
    name = input("请输入姓名")
    id_card = input('请输入身份证')
    if len(id_card) == 18 and len(name) < 5 and len(name) > 1:
        address = "陈桥村溪口巷2号"
        area_code = id_card[:6]
        regional_information = constant.area[area_code]
        print(regional_information + address)
