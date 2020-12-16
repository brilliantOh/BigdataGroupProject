# operation.py

import random

def calc():
    lst = [] # 초기화

    for i in range(7): # 감정 갯수만큼
        lst.append(random.randrange(1, 100)) # 1이상 100미만의 정수

    return lst