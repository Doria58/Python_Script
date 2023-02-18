# -*- coding = utf-8 -*-
# @time:2023/2/5 16:37
# Author:He H

import random
import numpy as np
from tkinter import messagebox
import tkinter

gacha = [i for i in range(1, 10001, 1)]  # 总池子,一共1W个元素
Five_Star_Pool = [i for i in range(10000, 9940, -1)]  # 抽中五星的池子,74抽以前概率为0.6%，即60个元素
Up_Star_Pool = []

gacha = np.array(gacha)
Five_Star_Pool = np.array(Five_Star_Pool)
Up_Star_Pool = np.array(Up_Star_Pool)
five_count = 0
ne_count = 0
five_sequence = 0
Hero = ['刻晴', '琴', '提纳里', '七七', '莫娜', '迪卢克']

def roll_single(number):  # 1-73抽的算法机制
    global Up_Star_Pool, five_count, ne_count, Five_Star_Pool , five_sequence
    rol = random.randrange(0, 9999, 1)  # 随机0-9999，gacha池子的索引
    rol_result = gacha[rol]
    ne_count = ne_count + number
    # print(f'五星池中有{len(Five_Star_Pool)}个元素了')

    if 0 < ne_count <= 73:
        if rol_result in Five_Star_Pool:
            print(f'第{ne_count}抽出金')
            five_sequence = ne_count
            ne_count = 0
            Five_Star_Pool_number = len(Five_Star_Pool)
            for i in range(1, int((Five_Star_Pool_number / 2) + 1), 1):
                Up_Star_Pool = np.append(Up_Star_Pool, '胡桃')  # Up人物
            for i in range(1, 6, 1):
                for j in range(0, 6, 1):
                    Up_Star_Pool = np.append(Up_Star_Pool, Hero[j])
            up_rol = random.randrange(0, len(Up_Star_Pool), 1)
            ''' 保底机制 '''
            if five_count == 0:
                up_result = Up_Star_Pool[up_rol]
                if up_result != '胡桃':
                    five_count = 1
            else:
                up_result = '胡桃'
                five_count = 0
            return up_result, five_sequence
        else:
            return '答辩', five_sequence
    elif 89 >= ne_count >= 74:
        beilv = ne_count - 73
        Five_Star_Pool = []
        Five_Star_Pool = [i for i in range(10000, 9940, -1)]
        for i in range(1, ((beilv * 600) + 1), 1):
            Five_Star_Pool = np.append(Five_Star_Pool, i)
        # print(f'五星池中有{len(Five_Star_Pool)}个元素了')
        if rol_result in Five_Star_Pool:
            print(f'第{ne_count}抽出金')
            ne_count = 0
            Five_Star_Pool = [i for i in range(10000, 9940, -1)]
            Five_Star_Pool_number = len(Five_Star_Pool)
            for i in range(1, int((Five_Star_Pool_number / 2) + 1), 1):
                Up_Star_Pool = np.append(Up_Star_Pool, '胡桃')  # Up人物
            for i in range(1, 6, 1):
                for j in range(0, 6, 1):
                    Up_Star_Pool = np.append(Up_Star_Pool, Hero[j])
            up_rol = random.randrange(0, len(Up_Star_Pool), 1)
            ''' 保底机制 '''
            if five_count == 0:
                up_result = Up_Star_Pool[up_rol]
                if up_result != '胡桃':
                    five_count = 1
            else:
                up_result = '胡桃'
                five_count = 0
            return up_result, five_sequence
        else:
            return '答辩', five_sequence

    elif ne_count == 90:
        five_sequence = ne_count
        ne_count = 0
        Five_Star_Pool_number = len(Five_Star_Pool)
        for i in range(1, int((Five_Star_Pool_number / 2) + 1), 1):
            Up_Star_Pool = np.append(Up_Star_Pool, '胡桃')  # Up人物
        for i in range(1, 6, 1):
            for j in range(0, 6, 1):
                Up_Star_Pool = np.append(Up_Star_Pool, Hero[j])
        up_rol = random.randrange(0, len(Up_Star_Pool), 1)
        ''' 保底机制 '''
        if five_count == 0:
            up_result = Up_Star_Pool[up_rol]
            if up_result != '胡桃':
                five_count = 1
        else:
            up_result = '胡桃'
            five_count = 0
        return up_result, five_sequence


def roll_ten(number):
    global Up_Star_Pool, five_count ,five_sequence
    ten_result = []
    for i in range(1, number + 1, 1):
        sin_rol = roll_single(1)[0]
        ten_result.append(sin_rol)
    return ten_result, five_sequence
