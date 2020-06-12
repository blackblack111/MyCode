# -*- coding:utf-8 -*-

import requests
import urllib.parse


with open(r'E:\projects\meirenyu\recording.txt','r',encoding='gbk') as f:
    all = f.readlines()

for one in all:
    sentence = one.strip()
    composed = urllib.parse.quote(sentence)
    # print(composed)

    url = 'https://www.bing.com/tspeak?&format=audio%2Fmp3&language=zh-CN&IG=D95470137CC5452C87A7A12CC1BA2300&IID=translator.5038.5&options=male&text='+composed

    resp = requests.get(url)

    filename = sentence+'.mp3'
    with open(filename,'wb') as f:
        f.write(resp.content)
        print(sentence)

