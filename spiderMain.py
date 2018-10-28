# -*- coding: utf-8 -*-
import urlManger as urlM
import categories as cateG
import htmlDownloader as htmlD
import htmlParser as htmlP
from dataOutput import DataOutput
import threading
class SpyderMain(object):

    def __init__(self,root_url,category_Nums,categories_Name,path):
        self.searchUrlsManger=urlM.UrlManager()
        self.crawlUrlsManger=urlM.UrlManager()
        self.htmlParser = htmlP.HtmlParser()
        ## construct the seach urls
        for pagesNum in range(int(category_Nums/10)):
            self.searchUrlsManger.add_new_url(root_url+"word="+categories_Name+"&pn="+str(pagesNum*10))
        
        htmlDownloader = htmlD.HtmlDownloader()
                ## search all the questions
        tmp_datas=[]
        dataOutput = DataOutput()
        for i in range(self.searchUrlsManger.get_urls_num()):
            tmp_searchUrl=self.searchUrlsManger.get_new_url()
            tmp_content=htmlDownloader.download(tmp_searchUrl)
            tmp_data=self.htmlParser.parse(tmp_content,i)
            tmp_datas.extend(tmp_data)
        dataOutput.output_excel(tmp_datas,path)
                
def runSpider(root_url,category_Nums,categories_Name,path):
    obj_spider=SpyderMain(root_url,category_Nums,categories_Name,path)

if __name__=='__main__':
    categories=cateG.Categories().getcategories()
    root_url=r"https://zhidao.baidu.com/search?"
    # 每个类别需要爬去的回答数
    threads = []
    paths=[]
    category_Nums=750

    # cate="父母体检"
    # path="D:\\Works\\datas\\"+cate+"百度知道体检知识.xlsx"
    # runSpider(root_url,category_Nums,"父母体检",path)
    for category in categories:
        path="./outputFiles/百度知道-" + category + ".xlsx"
        paths.append(path)
        t= threading.Thread(target=runSpider,args=(root_url,category_Nums,category,path))
        threads.append(t)

    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()