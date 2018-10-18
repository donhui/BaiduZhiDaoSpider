# BaiduZhiDaoSpider

Suppose: build this baiduzhidao Spider to get data from baidu zhidao
Ways to use: 
	1.edit the file "categories.txt" in the "readFiles"(use commas as intervals for writing)
	2.the run the "spiderMain.py" script,get all the excel files in the "outputFiles"
	3.run the "fileIntegration.py"script,get the integrated file.

Project Detials:
1.Divide the spider into serval modules:
	1).class Categories: manage the key words you want to search (easy to adapt the multithreaded program)
	2).class UrlManger: manage the urls needed to crawl (avoid duplication in datas)
	3).class HtmlDownloader: responsible for downloading the file on the internet and decode in "utf-8" which shows correct in Chinese.
	4).class HtmlParser: analyse the content downloaded from the internet (which can change to suit different website)
	5).class DataOutput: save the data needed in "*.xlsx" or "*.html" format
	6).class fileIntegration: read all the temp files and integrate them into one final file
