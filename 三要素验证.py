from id_validator import validator
import re

pattern = re.compile(r'^(13[0-9]|14[0|5|6|7|9]|15[0|1|2|3|5|6|7|8|9]|'
                     r'16[2|5|6|7]|17[0|1|2|3|5|6|7|8]|18[0-9]|'
                     r'19[1|3|5|6|7|8|9])\d{8}$')

while True:
    name = input('请输入姓名')
    sfz = input('请输入身份证')
    phone = input('请输入手机号')
    a = validator.is_valid(sfz)
    if a is True and len(name) >= 2 and len(name) <= 4 and len(phone) == 11 and pattern.search(phone) and phone.isnumeric() and sfz.isnumeric():
        print('验证通过')
    else:
        print('验证不通过')