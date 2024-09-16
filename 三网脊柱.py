from datetime import datetime, timedelta
import re
import random
import constant as const
import time

class IdNumber(str):

    def __init__(self, id_number):
        super(IdNumber, self).__init__()
        self.id = id_number
        self.area_id = int(self.id[0:6])
        self.birth_year = int(self.id[6:10])
        self.birth_month = int(self.id[10:12])
        self.birth_day = int(self.id[12:14])

    def get_area_name(self):
        return const.AREA_INFO[self.area_id]

    def get_birthday(self):
        return "{0}-{1}-{2}".format(self.birth_year, self.birth_month, self.birth_day)

    def get_age(self):
        now = (datetime.now() + timedelta(days=1))
        year, month, day = now.year, now.month, now.day

        if year == self.birth_year:
            return 0
        else:
            if self.birth_month > month or (self.birth_month == month and self.birth_day > day):
                return year - self.birth_year - 1
            else:
                return year - self.birth_year

    def get_sex(self):
        return int(self.id[16:17]) % 2

    def get_check_digit(self):
        check_sum = 0
        for i in range(0, 17):
            check_sum += ((1 << (17 - i)) % 11) * int(self.id[i])
        check_digit = (12 - (check_sum % 11)) % 11
        return check_digit if check_digit < 10 else 'X'

    @classmethod
    def verify_id(cls, id_number):
        if re.match(const.ID_NUMBER_18_REGEX, id_number):
            check_digit = cls(id_number).get_check_digit()
            return str(check_digit) == id_number[-1]
        else:
            return bool(re.match(const.ID_NUMBER_15_REGEX, id_number))

    @classmethod
    def generate_id(cls, sex=0):

        id_number = str(random.choice(list(const.AREA_INFO.keys())))
        start, end = datetime.strptime("1960-01-01", "%Y-%m-%d"), datetime.strptime("2000-12-30", "%Y-%m-%d")
        birth_days = datetime.strftime(start + timedelta(random.randint(0, (end - start).days + 1)), "%Y%m%d")
        id_number += str(birth_days)
        id_number += str(random.randint(10, 99))
        id_number += str(random.randrange(sex, 10, step=2))
        return id_number + str(cls(id_number).get_check_digit())


while True:
    print('请输入要查询的手机号')
    a = input()
    try:
        b = int(a)
        b = len(a)
        if b == 11:
            if __name__ == '__main__':
                random_sex = random.randint(0, 1)
            print('查询中')
            time.sleep(3)
            print('查询成功！身份证如下')
            print(IdNumber.generate_id(random_sex))
        else:
            print('错误')
    except:
        print('错误')