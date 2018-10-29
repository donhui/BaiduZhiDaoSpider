import os
from categories import Categories

categories=Categories().getcategories()

for category in categories:
    path="./outputFiles/百度知道-"+category+".xlsx"
    if not os.path.exists(path):
        print(category)
