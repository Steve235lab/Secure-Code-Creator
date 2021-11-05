# -*- coding: utf-8 -*-
"""
Secure Code Creator

Created on Mon Jun 22 22:49:22 2020

@author: Steve D. J.

Copyright (c) 2020 Steve D. J..All rights reserved.
"""


def SepLine():  #输出分割线
    print("\n==========================================\n")


def create_txt():   #生成大文件
    import time
    import numpy as np
    global txt_title
    print("正在生成安全文件...\n因为文件较大，该过程可能需要花费几分钟。\n")
    loc_time = time.localtime()
    loc_time = time.strftime("%Y_%m_%d_%Hh%Mm%Ss", loc_time)
    txt_title = loc_time + 'scf.txt'
    base = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
    base_len = len(base)
    txt_value = 'Remember the following words, which will be a part of your QQ sign in code.\n'     #信你个鬼！
    for j in range(0,20): #820MB左右
        for k in range(0,1024): #500MB
            for l in range(0,1024): #KB
                base_index = np.random.randint(0,base_len)
                txt_value = txt_value + base[base_index]
        with open('D:\\' + txt_title,'a',encoding='utf-8') as f:
            f.write(txt_value)
            f.close()
    print("已生成文件，路径为D:\\" + txt_title + "。请保留此文件以备后续查看密码。\n")


def print_16code(): #大文件MD5值计算
    import hashlib
    import os
    import datetime
    
    def GetFileMd5(filename):
        if not os.path.isfile(filename):
            return
        myhash = hashlib.md5()
        f = open(filename,'rb')
        while True:
            b = f.read(8096)
            if not b :
                break
            myhash.update(b)
        f.close()
        return myhash.hexdigest()
    
    if key == 'A':
        filepath = input('请输入安全文件路径：(将文件直接拖入该窗口即可)\n')
        
    if key == 'B':
        filepath = 'D:\\' + txt_title
    
    # 输出文件的md5值以及记录运行时间
    starttime = datetime.datetime.now()
    MD5 = str(GetFileMd5(filepath))[0:16]
    print ('您的密码为 ' + MD5)
    endtime = datetime.datetime.now()
    if key == 'A':
        print ('运行时间：%ds\n'%((endtime-starttime).seconds)) 
    print("为保证密码绝对安全，请勿将此密码保存于本地，并定期更换密码。")


SepLine()    
print("Copyright (c) 2020 Steve D. J.. All rights reserved.\n")
SepLine()  

print("声明：\n1. 本程序绝无任何窃取用户隐私的功能与病毒进程，请放心使用。\n2. 本程序通过生成大文件并将大文件MD5值的前十六位输出作为参考密码，可有效防止盗号木马。\n3. 该程序生成的密码仅作参考，具体改密过程仍需用户自行登录QQ安全中心进行操作。\n4. 本程序秉承开源精神，仅作学习交流使用，作者不承担任何可能的因为使用该程序引发的后果。\n继续使用本程序即表示您已认真阅读并认可上述声明。\n")  


while True:
    
    print("A: 查看密码\nB: 修改密码\nexit: 退出程序\n")
    key = input('键入 A 或 B 并回车以继续:\n')
    
    if key == 'exit':
        break
    
    elif key == 'A':
        print_16code()
        SepLine()    
        
    elif key == 'B':
        flag = input("即将在D盘生成安全文件，请确保D盘有足够空间！\n键入'Y'并回车以继续:\n")
        if flag == 'Y':
            create_txt()
            print_16code()
            print("请前往QQ安全中心将QQ密码更改为此密码！\n")
            SepLine()
        
    else:
        SepLine()

        
