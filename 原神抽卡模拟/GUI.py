# -*- coding = utf-8 -*-
# @time:2023/2/5 16:29
# Author:He H
from tkinter import messagebox

from rolls_method import *


def rolls_single():
    global count, rough, show_list
    count = count + 1

    def jug():  # 显示抽取结果
        global rough, count
        rough = rough - 160
        count_var_label.set(f"目前抽取次数：{count}")
        rough_var_lable.set(f"当前原石数：{rough}")
        if rough < 0:
            rough = rough + 160
            count = count - 1
            messagebox.showinfo(title='抽卡数', message='原石数不足！！！')
            text.insert(tk.END, '原石数不足！！！\n')
            text.see('end')
            rough_var_lable.set(f"当前原石数：{rough}")
            count_var_label.set(f"目前抽取次数：{count}")
            return rough
        else:
            # messagebox.showinfo(title='抽卡数', message=f'已经抽取了{count}抽,剩余原石:{rough},本次抽出 \n  {roll_result} 一个')
            if roll_result != '答辩':
                text.insert(tk.END, f' !!!出金 {count} 本次抽出 {roll_result} 一个 !!!\n')
                text.see('end')
                show_list.append(roll_result)
            else:
                text.insert(tk.END, f' {count} 本次抽出 {roll_result} 一个\n')
                text.see('end')
                show_list.append(roll_result)
        return count, rough, show_list

    roll_return = roll_single(1)
    roll_result = roll_return[0]
    roll_squence = roll_return[1]
    five_st_squence.append(roll_squence)
    jug()
    return count, rough, show_list


def rolls_ten():
    global count, rough, show_list, five_st_squence

    if rough < 1600:
        messagebox.showinfo(title='抽卡数', message=f'剩余原石:{rough},原石数不足！！！')
        return count
    else:
        roll_return = roll_ten(10)
        roll_result = roll_return[0]
        roll_squence = roll_return[1]
        five_st_squence.append(roll_squence)
        for item in range(1, 11, 1):
            count = count + 1
            rough = rough - 160
            text.insert(tk.END, f' {count} 本次抽出 {roll_result[item - 1]} 一个\n')
            text.see('end')
            show_list.append(roll_result[item - 1])
    count_var_label.set(f"目前抽取次数：{count}")
    rough_var_lable.set(f"当前原石数：{rough}")
    # messagebox.showinfo(title='抽卡数', message=f'已经抽取了{count}抽,剩余原石:{rough},本次抽出 \n {ten_text}')
    return count, show_list


def get_text():
    def get_rough_text():
        global rough
        Input_rough = Input_Window.get('1.0', 'end')
        rough = int(Input_rough) + rough
        rough_var_lable.set(f"当前原石数：{rough}")
        Input_Window.delete('1.0', 'end')
        window_Enty.destroy()

    global rough
    window_Enty = tk.Tk()
    window_Enty.title('充值窗口————Author:He H')  # 窗口标题
    window_Enty.geometry('400x100')  # 设置窗口大小:宽x高 f'{Scree_W}x{Scree_H}'
    window_Enty.iconbitmap('pic\\Ghost.ico')  # 更no more room in hell改左上角窗口的的icon图标
    Input_Window = tk.Text(window_Enty, height=1.5, width=30)
    Input_Window.pack()
    tk.Button(window_Enty, text='充值', command=get_rough_text, font=('宋体', 20)).pack(padx=5, pady=5)

    window_Enty.mainloop()
    return rough


def show_history():
    global show_list, count, five_st_squence
    five_result = []
    four_result = []
    for item in range(0, len(show_list), 1):
        if show_list[item] == '答辩':
            four_result.append(show_list[item])
        else:
            five_result.append(show_list[item])
    five_result_text = ' '.join(five_result)
    four_result_text = ' '.join(four_result)
    messagebox.showinfo(title='抽卡历史',
                        message=f'目前已经抽取了{count}抽 \n 五星角色为: \n {five_result_text} \n 四星物品为:\n{four_result_text}')

import tkinter as tk
from tkinter import *

rough = 20000  # 原石数
count = 0
show_list = []
five_st_squence = []
Gacha_Things = ['刻晴', '琴', '提纳里', '七七', '莫娜', '迪卢克', '胡桃', '答辩']

root_window = tk.Tk()  # 创建Window窗口对象

Scree_W = int(root_window.winfo_screenwidth() / 2)
Scree_H = int(root_window.winfo_screenheight() / 2)  # 获取当前电脑屏幕分辨率，并确保以一半的分辨率创建新窗口
# root_window.resizable(False, False)  # 设置窗口是否可拉伸，0,0代表不可拉伸

root_window.title('原神抽卡模拟器————Author:He H')  # 窗口标题
root_window.geometry('576x576')  # 设置窗口大小:宽x高 f'{Scree_W}x{Scree_H}'
root_window.iconbitmap('pic\\Ghost.ico')  # 更no more room in hell改左上角窗口的的icon图标
root_window['background'] = '#FAEBD7'  # 设置主窗口的背景颜色,颜色值可以是英文单词，或者颜色值的16进制数

blackPic = Canvas(root_window, bg="blue")
filename = PhotoImage(file='pic\\blackground.png')  # 背景图片设置
background_label = Label(root_window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

tk.Label(root_window, text='赤团开时', bg='Yellow', fg='Red', font=('楷体', 50)).pack()  # 添加文本内容,设置字体的前景色和背景色，和字体类型、大小

text = tk.Text(root_window, height=5, width=30)
text.pack()

count_var_label = tk.StringVar()
add_one = tk.StringVar()
add_ten = tk.StringVar()  # 变量文字设置
rough_var_lable = tk.StringVar()

rough_lable = tk.Label(root_window, textvariable=rough_var_lable, fg='Red', font=('宋体', 40))
rough_var_lable.set(f"当前原石数：{rough}")
rough_lable.pack()

count_label = tk.Label(root_window, textvariable=count_var_label, font=('宋体', 30, 'bold'))
count_var_label.set("目前抽取次数：0")
count_label.pack(padx=10, pady=10)

tk.Button(root_window, text='抽1发', command=rolls_single, font=('宋体', 30)).pack(side='left')
tk.Button(root_window, text='抽10发', command=rolls_ten, font=('宋体', 30)).pack(side='right')
tk.Button(root_window, text='充值', command=get_text, font=('宋体', 30)).pack(padx=5, pady=5)
tk.Button(root_window, text='退出', command=root_window.quit, font=('宋体', 30)).pack(side='bottom')
tk.Button(root_window, text='历史', command=show_history, font=('宋体', 30)).place(anchor='se', x=576, y=576)
# tk.Button(root_window, text='Play Radio', command=play_vidio, font=('宋体', 30)).place(anchor='se', x=300, y=500)
tk.mainloop()
