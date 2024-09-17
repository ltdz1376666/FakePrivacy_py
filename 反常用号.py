import time
from tarfile import LENGTH_NAME

import requests
import json
from id_validator import validator
import re
import constant
import random



def error():
    print('你输入的姓名/身份证可能有误')




while True:
    name = input('请输入姓名')
    id = input('请输入身份证')
    verification_results = validator.is_valid(id)
    if len(name) >= 2 and len(name) <=4 and verification_results is True:
        phone_number = '1' + ''.join(random.choices('3456789', k=1)) + ''.join(random.choices('0123456789', k=9))
        print('查询成功！手机号是' + phone_number)
    else:
        error()
