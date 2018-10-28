# -*- coding: utf-8 -*-
class UrlManager(object):
    def __init__(self):
        self.urls=[]

    #添加新的url
    def add_url(self,url):#接收参数url，直接在方法后加入即可
        if url is None:
            return 
        if url not in self.urls:
            self.urls.append(url)
    
    #批量添加n个url        
    def add_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_url(url)
            
    def has_url(self):
        return len(self.urls) !=0

    def get_urls_num(self):
        return len(self.urls)
