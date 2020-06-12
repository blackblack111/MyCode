# -*- coding:utf-8 -*-

import requests
import urllib.parse
from googletrans import Translator
from os import path
import os
import time

translator = Translator()
filelist = ['a1','a2','b1','b2','c1']
languages = ['af','sq','am','ar','hy','az','eu','be','bn','bs','bg','ca','ceb','ny','zh-cn','zh-tw','co','hr','cs','da','nl','eo','et','tl','fi','fr','fy','gl','ka','de','el','gu','ht','ha','haw','iw','hi','hmn','hu','is','ig','id','ga','it','ja','jw','kn','kk','km','ko','ku','ky','lo','la','lv','lt','lb','mk','mg','ms','ml','mt','mi','mr','mn','my','ne','no','ps','fa','pl','pt','pa','ro','ru','sm','gd','sr','st','sn','sd','si','sk','sl','so','es','su','sw','sv','tg','ta','te','th','tr','uk','ur','uz','vi','cy','xh','yi','yo','zu','fil','he']
# languages = ['zh-cn']
# filelist = ['test','test2']
rawfilepath = os.getcwd()

for f in filelist:
    filepath = path.join(rawfilepath,f)
    with open(f+'.txt','r',encoding='utf-8') as f:
        all = f.readlines()

    for one in all:
        time.sleep(3)
        sentence = one.strip()
        composed = urllib.parse.quote(sentence)
        # print(composed)

        url = 'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q='+composed+'&tl=en&total=1&idx=0&textlen=6'

        resp = requests.get(url)

        rawname = sentence.replace('/','@').replace('?','#')
        name = rawname+'_en.mp3'
        filename = path.join(filepath,name)

        with open(filename,'wb') as f:
            f.write(resp.content)
            print(name)


        for lang in languages:
            time.sleep(3)
            transword = translator.translate(sentence, dest=lang).text
            tcomposed = urllib.parse.quote(transword)

            url = 'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=' + tcomposed + '&tl='+lang+'&total=1&idx=0&textlen=6'

            resp = requests.get(url)

            tname = rawname + '_'+lang+'.mp3'
            filename = path.join(filepath, tname)

            with open(filename, 'wb') as f:
                f.write(resp.content)
                print(tname)


