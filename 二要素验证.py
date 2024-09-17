import requests
import json
from id_validator import validator

#陆光良制作


def error():
    print('你输入的姓名/身份证可能有误')



while True:
    realname = input("请输入用户真实姓名：")
    identityNumber = input("请输入用户身份证号码：")
    if len(identityNumber) == 18 and len(realname) < 5 and len(realname) > 1:
        try:
            a = validator.is_valid(identityNumber)
            if a is True:
                print('验证通过')
            else:
                print("验证不通过")
        except:
            error()
    else:
        error()