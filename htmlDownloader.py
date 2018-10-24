# -*- coding: utf-8 -*-
import requests
import re

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept - Encoding':'gzip, deflate, br',
               'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
               'Connection':'Keep-Alive',
               'Host':'zhidao.baidu.com',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
        req = requests.get(url,headers=headers)
        if req.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(req.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = req.apparent_encoding

            # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            global encode_content
            encode_content = req.content.decode(encoding, 'replace')  # 如果设置为replace，则会用?取代非法字符；
            encode_content=encode_content.encode('utf-8').decode('utf-8')
        regx = r"charset=gbk"
        result,number = re.subn(regx,"charset=uft-8",encode_content) 

        return result


