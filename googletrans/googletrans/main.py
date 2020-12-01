# -*- coding:utf-8 -*-

import requests
import execjs

def get_tk(text):
    with open('jsfunction.js','r',encoding='utf-8') as f:
        js = f.read()
    j = execjs.compile(js)
    return j.call('wu',text).replace('&tk=', '')


if __name__ == '__main__':

    text = 'log'
    url = 'https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=sos&dt=ss&dt=t&otf=1&ssel=0&tsel=0&kc=1&tk='+get_tk(text)+'&q='+text

    res = requests.get(url).json()[0][0][0]
    print(res)
