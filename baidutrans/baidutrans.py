# -*- coding:utf-8 -*-

import requests
import execjs
import re
import time
from urllib import parse

def get_tk(text):
    with open('baidu.js','r',encoding='utf-8') as f:
        js = f.read()
    j = execjs.compile(js)
    return j.call('e',text)


def trans(word):
    url = "https://fanyi.baidu.com/v2transapi"

    querystring = {"from":"en","to":"zh"}

    # word = word.replace('\n','').replace('\r','').replace('\t','')

    parsedword = parse.quote(word)
    payload = "from=en&to=zh&query="+parsedword+"&transtype=realtime&simple_means_flag=3&sign="+get_tk(word)+"&token=548b6f21c279e05c1e8752ac2fa479b7&domain=common"

    print(payload)

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "BIDUPSID=9504CF77198EC0C4E7CFBD0E54BC63B2; PSTM=1568265782; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=7A5EED8CE7165B8A609AAC95DB7EEF72:FG=1; BDUSS=t2cy1rMzBXd3BsNDNiLVpGVVZGOGVyaXdQclJiZ2U4R2lyMjRWflVsUDl6N2xmRVFBQUFBJCQAAAAAAAAAAAEAAAAjrAFd0KHLzrzStcTQocH1NzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP1Ckl~9QpJfem; BDUSS_BFESS=t2cy1rMzBXd3BsNDNiLVpGVVZGOGVyaXdQclJiZ2U4R2lyMjRWflVsUDl6N2xmRVFBQUFBJCQAAAAAAAAAAAEAAAAjrAFd0KHLzrzStcTQocH1NzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP1Ckl~9QpJfem; BAIDUID_BFESS=7A5EED8CE7165B8A609AAC95DB7EEF72:FG=1; MCITY=-131%3A; ZD_ENTRY=bing; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1608698911,1608706321; H_PS_PSSID=1459_33358_33306_33350_33313_33312_33311_33310_33231_33309_33308_33307_33144_33385_33370; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; __yjs_duid=1_e9b4d25e9e5cfefa03f5872adba720381608876890788; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1608876906; ab_sr=1.0.0_Zjk2YTcwMjYxNjQyMDY1NWE0MjFlNjZkOGE3N2Q1ODIyOTgxYjhlYmYzYTcyMmM4ZDY2OGEzMzFkYTVjNjk4ZDBlMjk4OGI1Y2NkODI0ZDdhNjU5NTE4NzA5MWJhZDY2; __yjsv5_shitong=1.0_7_a42625e64b407e6bd5ade54015726f2b914d_300_1608876904619_219.142.144.50_f062f69e; yjs_js_security_passport=b802de11e5d7aa7197a192623ab867d5e7cda813_1608876905_js",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",

        }

    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers, params=querystring)
    resp = response.json()
    print(resp)
    return resp['trans_result']['data'][0]['dst']

def Baidutranslate(rawword):
    # highpoints = re.compile(u'['u'\U0001F300-\U0001F64F' u'\U0001F680-\U0001F6FF'u'\u2600-\u2B55]+')
    highpoints = re.compile(u'['u'\U00010000-\U000FFFFF' u'\U0001F680-\U0001F6FF'u'\u2600-\u2B55]+')
    word = highpoints.sub(u'', rawword)
    process = word.replace('\n', r'\n').replace('\r',r'\r').replace('\t',r'\t')

    try:
        cn = trans(process).replace(r'\n', '\n').replace(r'\r', '\r').replace(r'\t', '\t')
    except:
        time.sleep(60)

        cn = trans(process).replace(r'\n', '\n').replace(r'\r', '\r').replace(r'\t', '\t')


    return cn


if __name__ == '__main__':
    word = 'The S&P500 is up over 10%, with the Nasdaq rising about 40%, from just over 9,000 on January 1, to close to 13,000 today.'

    print(get_tk(word))
    res = Baidutranslate(word)


    # print(word)
    # print(process)
    print(res)
