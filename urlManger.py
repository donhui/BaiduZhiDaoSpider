class UrlManager(object):
    #初始化两个set ，分别存放新旧url
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()
    
    #添加新的url
    def add_new_url(self,url):#接收参数url，直接在方法后加入即可
        if url is None:
            return 
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    
    #批量添加n个url        
    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
            
    def has_new_url(self):
        return len(self.new_urls) !=0  

    def get_urls_num(self):
        return len(self.new_urls)

    def get_new_url(self):
        new_url=self.new_urls.pop()#从set集合中取走这个url
        self.old_urls.add(new_url)
        return new_url
    
    def clear_all_urls(self):
        self.new_urls.clear()
