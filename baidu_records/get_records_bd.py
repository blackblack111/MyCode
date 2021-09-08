# -*- coding: utf-8 -*-

import requests
import base64

# url
# https://cloud.baidu.com/product/speech/tts_online?track=cp:nsem|pf:PC|pp:nsem-liuliang-zhuanan-AIzaixianyuyinhecheng|pu:yuyinhecheng-tongyongci|ci:|kw:10241920&renqun_youhua=2781229

# 文字转音频
text = '但是操作不方便'
# 音库种类
voice = '4103'

url = "https://cloud.baidu.com/aidemo"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\ntns\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"per\"\r\n\r\n"+voice+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"spd\"\r\n\r\n5\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"pit\"\r\n\r\n5\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"vol\"\r\n\r\n5\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"aue\"\r\n\r\n6\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"tex\"\r\n\r\n"+text+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",

    }

response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers).json()

url = response['data']
print(url)

url = url.replace('data:audio/x-mpeg;base64,','')
ori_image_data = base64.b64decode(url)
with open('test.mp3','wb') as f:
    f.write(ori_image_data)