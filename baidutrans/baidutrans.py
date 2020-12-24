# -*- coding:utf-8 -*-

import requests
import execjs
import re

def get_tk(text):
    with open('baidu.js','r',encoding='utf-8') as f:
        js = f.read()
    j = execjs.compile(js)
    return j.call('e',text)


def trans(word):
    url = "https://fanyi.baidu.com/v2transapi"

    querystring = {"from":"en","to":"zh"}

    # word = word.replace('\n','').replace('\r','').replace('\t','')

    payload = "from=en&to=zh&query="+word+"&transtype=realtime&simple_means_flag=3&sign="+get_tk(word)+"&token=548b6f21c279e05c1e8752ac2fa479b7&domain=common"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "BIDUPSID=9504CF77198EC0C4E7CFBD0E54BC63B2; PSTM=1568265782; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=7A5EED8CE7165B8A609AAC95DB7EEF72:FG=1; BDUSS=t2cy1rMzBXd3BsNDNiLVpGVVZGOGVyaXdQclJiZ2U4R2lyMjRWflVsUDl6N2xmRVFBQUFBJCQAAAAAAAAAAAEAAAAjrAFd0KHLzrzStcTQocH1NzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP1Ckl~9QpJfem; BDUSS_BFESS=t2cy1rMzBXd3BsNDNiLVpGVVZGOGVyaXdQclJiZ2U4R2lyMjRWflVsUDl6N2xmRVFBQUFBJCQAAAAAAAAAAAEAAAAjrAFd0KHLzrzStcTQocH1NzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP1Ckl~9QpJfem; BAIDUID_BFESS=7A5EED8CE7165B8A609AAC95DB7EEF72:FG=1; MCITY=-131%3A; ZD_ENTRY=bing; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; H_PS_PSSID=1459_33358_33306_33350_33313_33312_33311_33310_33231_33309_33308_33307_33144_33385; BA_HECTOR=2g04048h8ga5212k0j1fu5q8e0q; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1608698911,1608706321; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1608706321; ab_sr=1.0.0_ZmFmZWE4ZGM0NGQzZTJlNGYxYTljNzUyZWVlOWIxY2M0MGRkMjc0N2VjNThmODY4MDRmODJmZmI2ZmY4ZDYzYzhmMzNjYTk3YzllODgxMGUxMDMyZDM4OGRmNjhiYmIx; __yjsv5_shitong=1.0_7_a42625e64b407e6bd5ade54015726f2b914d_300_1608706320722_219.142.144.50_8b277583; yjs_js_security_passport=c4fb682a969252cd78c44ef190f2211f21b969b5_1608706321_js",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",

        }

    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers, params=querystring)
    resp = response.json()
    return resp['trans_result']['data'][0]['dst']

def Baidutranslate(rawword):
    # highpoints = re.compile(u'['u'\U0001F300-\U0001F64F' u'\U0001F680-\U0001F6FF'u'\u2600-\u2B55]+')
    highpoints = re.compile(u'['u'\U00010000-\U000FFFFF' u'\U0001F680-\U0001F6FF'u'\u2600-\u2B55]+')
    word = highpoints.sub(u'', rawword)
    process = word.replace('\n', r'\n').replace('\r',r'\r').replace('\t',r'\t')
    try:
        cn = trans(process).replace(r'\n', '\n').replace(r'\r','\r').replace(r'\t','\t')
        return cn
    except:
        return None


if __name__ == '__main__':
    word = 'The above list is probably a fantasy! 🤣 We are all working on something.'
    res = Baidutranslate(word)


    # print(word)
    # print(process)
    print(res)
