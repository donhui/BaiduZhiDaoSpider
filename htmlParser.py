from lxml import etree
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
            print(tmp_url)
            if str(tmp_url).startswith("http://zhidao.baidu.com") or str(tmp_url).startswith("https://zhidao.baidu.com"):
                tmp_content = ""
                try:
                    tmp_content=self.htmlDownloader.download(tmp_url)
                except Exception as e:
                    print(e)
                if tmp_content != "":
                    tmp_etree=etree.HTML(tmp_content)

                    # 问题
                    if(len(tmp_etree.xpath('//*[@id="wgt-ask"]/h1/span'))!=0):
                        tmp_question=tmp_etree.xpath('//*[@id="wgt-ask"]/h1/span')[0].text
                    else:
                        tmp_question=""
                    print(tmp_question)

                    # 问题详情
                    if (len(tmp_etree.xpath('//*[@id="wgt-ask"]/div/span')) != 0):
                        tmp_question_detail = tmp_etree.xpath('//*[@id="wgt-ask"]/div/span')[0].text
                    else:
                        tmp_question_detail = ""

                    # 回答总数
                    if (len(tmp_etree.xpath('//*[@class="question-all-answers-title"]')) != 0):
                        answers_count = tmp_etree.xpath('//*[@class="question-all-answers-title"]')[0].text
                    else:
                        answers_count = ""

                    # 回答
                    # 判断是否存在best answer
                    best_answer_id= re.findall("best-content-\d+",str(tmp_content))
                    tmp_id=""
                    tmp_answer_content= ""
                    # 点赞数
                    tmp_evaluate_good_num=""
                    # 踩数
                    tmp_evaluate_terrible_num=""

                    # 最佳答案
                    if(len(best_answer_id) != 0):
                        best_answer=tmp_etree.xpath('//*[@id="'+best_answer_id[0]+'"]')[0]
                        all_content=etree.tostring(best_answer,encoding = "utf-8", pretty_print = True, method = "html").decode('utf-8')
                        tmp_id= re.findall('best-content-\d+',str(all_content))[0].split('-')[-1]
                        good_rules='//*[@id="evaluate-'+tmp_id+'"]/@data-evaluate'
                        bad_rules='//*[@id="evaluate-bad-'+tmp_id+'"]/@data-evaluate'
                        tmp_evaluate_good_num = tmp_etree.xpath(good_rules)[0]
                        tmp_evaluate_terrible_num = tmp_etree.xpath(bad_rules)[0]
                        tmp_answer_content = all_content.split('</div>')[-2]

                        reply_date_rules='//*[@id="wgt-replyer-all-'+tmp_id+'"]/span/span[last()]'
                        reply_date = tmp_etree.xpath(reply_date_rules)[0].text.replace("推荐于","")

                        is_best_answer = "最佳答案"

                        # ['类别', '问题', '问题详情', '回答总数', '回答', '回答时间','点赞数', '踩数'，'最佳答案']

                        tmp_information = [tmp_category, tmp_question, tmp_question_detail, answers_count,
                                           tmp_answer_content, reply_date,
                                           tmp_evaluate_good_num,tmp_evaluate_terrible_num, is_best_answer]
                        self.datas.append(tmp_information)

                    # 普通答案
                    answers_id_arr=re.findall("answer-content-\d+",str(tmp_content))
                    if(len(answers_id_arr)!=0):
                            for answers_id in answers_id_arr:
                                answer=tmp_etree.xpath('//*[@id="'+answers_id+'"]')[0]
                                all_content=etree.tostring(answer,encoding = "utf-8", pretty_print = True, method = "html").decode('utf-8')
                                tmp_answer_content.encode('utf-8').decode('utf-8')
                                tmp_id= re.findall('answer-content-\d+',str(all_content))[0].split('-')[-1]
                                good_rules='//*[@id="evaluate-'+tmp_id+'"]/@data-evaluate'
                                bad_rules='//*[@id="evaluate-bad-'+tmp_id+'"]/@data-evaluate'
                                tmp_evaluate_good_num = tmp_etree.xpath(good_rules)[0]
                                tmp_evaluate_terrible_num = tmp_etree.xpath(bad_rules)[0]
                                tmp_answer_content = all_content.split('</div>')[-2]

                                reply_date_rules = '//*[@id="wgt-replyer-all-' + tmp_id + '"]/span/span[last()]'
                                reply_date = tmp_etree.xpath(reply_date_rules)[0].text.replace("推荐于","")

                                if (len(best_answer_id) != 0):
                                    tmp_question = ""
                                    tmp_question_detail = ""
                                    answers_count = ""
                                else:
                                    if answers_id != answers_id_arr[0]:
                                        tmp_question = ""
                                        tmp_question_detail = ""
                                        answers_count = ""
                                is_best_answer = ""

                                # ['类别','问题', '问题详情', '回答','点赞数','踩数', '最佳答案']

                                tmp_information = [tmp_category, tmp_question, tmp_question_detail, answers_count,
                                                   tmp_answer_content, reply_date,
                                                   tmp_evaluate_good_num, tmp_evaluate_terrible_num, is_best_answer]
                                self.datas.append(tmp_information)
        return self.datas