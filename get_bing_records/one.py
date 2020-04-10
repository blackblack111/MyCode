# -*- coding:utf-8 -*-

import requests
import urllib.parse

sentence = '鹅先生'
composed = urllib.parse.quote(sentence)


url = 'https://www.bing.com/tspeak?&format=audio%2Fmp3&language=zh-CN&IG=D95470137CC5452C87A7A12CC1BA2300&IID=translator.5038.5&options=male&text='+composed

resp = requests.get(url)

filename = sentence+'.mp3'
with open(filename,'wb') as f:
    f.write(resp.content)