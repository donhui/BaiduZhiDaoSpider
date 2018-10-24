# -*- coding: utf-8 -*-
class Categories:
    def __init__(self):
        self.new_categories = set()
        self.old_categories = set()
        self.getcategories()

    def add_new_category(self, category):  # 接收参数url，直接在方法后加入即可
        if category is None:
            return
        if category not in self.new_categories and category not in self.old_categories:
            self.new_categories.add(category)

    def add_new_categories(self, categories):
        if categories is None or len(categories) == 0:
            return
        for category in categories:
            self.add_new_category(category)

    def has_new_category(self):
        return len(self.new_categories) !=0  
    
    def new_category_num(self):
        return len(self.new_categories)

    def get_all_new_categories(self):
        return self.new_categories

    def get_new_category(self):
        new_category=self.new_categories.pop()#从set集合中取走这个url
        self.old_categories.add(new_category)
        return new_category

    def getcategories(self):
        categories = []
        with open('./readFiles/category.txt', 'r', encoding='utf-8') as f:
            categories = f.read().split(',')
        self.add_new_categories(categories)
        return(categories)    

