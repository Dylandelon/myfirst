#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2018/11/27 18:39
#@Author: zhangdelong
#@File  : anytextlog.py

import os
import os.path
import string

# txt_path = 'D:/youxinProjections/trafic-youxin/MobileNet_v1/obtain_qq_json_new/Crop_Ocr_txt/'
# des_txt_path = 'D:/youxinProjections/trafic-youxin/MobileNet_v1/obtain_qq_json_new/1000_simple_OCRtxts/'
txt_path = 'D:/cnnwork/pppp/old/'
des_txt_path = 'D:/cnnwork/pppp/new/'

txt_files = os.listdir(txt_path)  # txt_files能得到该目录下的所有txt文件的文件名


def select_simples():
    for txtfile in txt_files:
        if not os.path.isdir(txtfile):
            in_file = open(txt_path + txtfile, 'r')
            out_file = open(des_txt_path + txtfile, 'a') # 此处自动新建一个文件夹和txtfile的文件名相同,'a'为自动换行写入
            lines = in_file.readlines()
            tempLine =''
            tempIndex=0

            for index in range(len(lines)):
                line = lines[index]
                if '[5.1.1]' in line:
                    tempLine=line
                    tempIndex=index
                elif tempLine !='' and tempIndex == index-1 and '[5.5.1]' not  in line :
                    out_file.write(tempLine)  # 若包含子串，则将该行内容全部重新写入新的txt文件
                    out_file.write(line)  # 若包含子串，则将该行内容全部重新写入新的txt文件
                    print(tempLine)
                    print(line)
                else:
                    temp=''

            out_file.close()
if __name__ == '__main__':
    select_simples()

