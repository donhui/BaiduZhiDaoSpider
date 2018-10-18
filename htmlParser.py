from lxml import etree
from lxml.etree import *
import htmlDownloader as htmlD
import re
class HtmlParser(object):

    def __init__(self):
        self.all_hrefs = []
        self.htmlDownloader = htmlD.HtmlDownloader()
        self.datas=[]

    # 获取所有的a标签的url
    def get_all_href(self, html_content, page_num):
        self.all_hrefs.clear()
        self.page = etree.HTML(html_content)
        print("获取第%s个页面的链接...." %str(page_num+1))
        for i in range(1, 11):
            xpath='//*[@id="wgt-list"]/dl['+str(i)+']/dt/a/@href'
            if(len(self.page.xpath(xpath))!=0):
                self.all_hrefs.append(self.page.xpath(xpath)[0])
        # print("第%s个页面的所有链接"%str(page_num+1))
        # for i in self.all_hrefs:
        #     print (i)

    def parse(self, html_content, page_num):
        self.datas.clear()
        self.page = etree.HTML(html_content)
        tmp_category=self.page.xpath('//*[@id="kw"]/@value')[0]
        print('类别：'+tmp_category)
        self.get_all_href(html_content, page_num)
        for tmp_url in self.all_hrefs:
            tmp_content=self.htmlDownloader.download(tmp_url)
            tmp_etree=etree.HTML(tmp_content)
            # 问题
            if(len(tmp_etree.xpath('//*[@id="wgt-ask"]/h1/span'))!=0):
                tmp_question=tmp_etree.xpath('//*[@id="wgt-ask"]/h1/span')[0].text
            else:
                tmp_question=""
            # 回答
            # 判断是否存在best answer
            best_answer_id= re.findall("best-content-\d+",str(tmp_content))
            tmp_id=""
            tmp_answer_content= ""
            # 点赞数
            tmp_evaluate_good_num=""
            # 踩数
            tmp_evaluate_terrible_num=""
            if(len(best_answer_id) != 0):
                best_answer=tmp_etree.xpath('//*[@id="'+best_answer_id[0]+'"]')[0]
                all_content=etree.tostring(best_answer,encoding = "utf-8", pretty_print = True, method = "html").decode('utf-8')
                tmp_id= re.findall('best-content-\d+',str(all_content))[0].split('-')[-1]
                good_rules='//*[@id="evaluate-'+tmp_id+'"]/@data-evaluate'
                bad_rules='//*[@id="evaluate-bad-'+tmp_id+'"]/@data-evaluate'
                tmp_evaluate_good_num = tmp_etree.xpath(good_rules)[0]
                tmp_evaluate_terrible_num = tmp_etree.xpath(bad_rules)[0]
                tmp_answer_content = all_content.split('</div>')[-2]                
            else:
                first_answer_id=re.findall("answer-content-\d+",str(tmp_content))
                if(len(first_answer_id)!=0):
                    first_answer=tmp_etree.xpath('//*[@id="'+first_answer_id[0]+'"]')[0]
                    all_content=etree.tostring(first_answer,encoding = "utf-8", pretty_print = True, method = "html").decode('utf-8')
                    tmp_answer_content.encode('utf-8').decode('utf-8')
                    tmp_id= re.findall('answer-content-\d+',str(all_content))[0].split('-')[-1]
                    good_rules='//*[@id="evaluate-'+tmp_id+'"]/@data-evaluate'
                    bad_rules='//*[@id="evaluate-bad-'+tmp_id+'"]/@data-evaluate'
                    tmp_evaluate_good_num = tmp_etree.xpath(good_rules)[0]
                    tmp_evaluate_terrible_num = tmp_etree.xpath(bad_rules)[0]
                    tmp_answer_content = all_content.split('</div>')[-2]

            # ['类别','问题','回答','点赞数','踩数']

            tmp_information=[tmp_category,tmp_question,tmp_answer_content,tmp_evaluate_good_num,tmp_evaluate_terrible_num]
            self.datas.append(tmp_information)
        return self.datas
            
            
        
        