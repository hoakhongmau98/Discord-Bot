#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import os
import sys
import requests
from bs4 import BeautifulSoup
import Dict.findwords as findwords

url = 'http://cunghoc.vn/tkb/data/1_12_dx/HTML/tkb_class_7_0.html'

r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc, features="html.parser")
tr_tag = soup.find_all('tr')
# print(tr_tag)
"""
Mô tả vòng lặp 
Sẽ lặp 2 lần: 
Vòng lặp ngoài đưa vào các dòng của data.
Vòng lặp bên trong đưa ra các gợi ý để tìm kiếm ký tự đã được define, nếu có thì xuất ra từ ngữ chính xác tương ứng với
list theo thứ tự của vòng lặp đầu tiên
Bao quanh tất cả là 1 vòng lặp là một mảng lớn dạng numpy mang tất cả giá trị.
"""


list_tkb = [[] for y in range(len(tr_tag))]

list_str = str(tr_tag[0]).split('\n')

for i in range(len(tr_tag)):
    list_str = str(tr_tag[i]).split('\n')
    for x in list_str:
        for key, value in findwords.tkb_words.items():
            if x.find(key) != -1:
                a = value
                if x.find('Tin há') != -1:
                    a = 'Tin Học'
                elif x.find('TCAnh*') != -1:
                    a = 'TCAnh*'
                elif x.find('TCToÃ¡n*') != -1:
                    a = 'TCToan*'
                list_tkb[i].append(a)


# Truy Vấn
def tkb_today(text):
    # today = [2-3-4-5-6-7]
    tkb_out = []
    if text in findwords.day_of_week:
        for keys, values in findwords.day_of_week.items():
            if text in keys:
                numb = int(values)
                for j in list_tkb:
                    tkb_out.append(j[numb])
    if len(tkb_out) == 0:
        return "Nhập sai cú pháp"
    else:
        return f"""{tkb_out[0]} {', '.join(tkb_out[1:])}"""

