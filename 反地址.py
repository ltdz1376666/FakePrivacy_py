import time
import requests
import json
from id_validator import validator
import re
import constant




def error():
    print('你输入的姓名/身份证可能有误')



while True:
    name = input("请输入姓名")
    id_card = input('请输入身份证')
    if len(id_card) == 18 and len(name) < 5 and len(name) > 1:
        address = "陈桥村溪口巷2号"
        area_code = id_card[:6]
        try:
            regional_information = constant.area[area_code]
            print(regional_information + address)
        except:
            error()
    else:
        error()
