#encoding: utf-8

import uuid
import os
import sys
import pymongo 
from datetime import datetime
from bs4 import BeautifulSoup


reload(sys)
sys.setdefaultencoding('utf-8')
conn = pymongo.Connection('localhost',27017)
db = conn.dygod
for movie in db.dygod.find().limit(200):
    
    title = str(movie['title'])
    if u'游戏' in title or u'集' in title:
        continue

    body = BeautifulSoup(movie['content'])
    doc =  "".join(str(item) for item in body.findAll('p'))
    doc = doc.replace("[","").replace("style=\"COLOR: black\"","")


    doc += "".join(str(item) for item in body.findAll('a'))
    # doc = doc.replace("bgcolor=\"#fdfddf\"","")
    # print doc
    doc = BeautifulSoup( doc )

    name = datetime.now().strftime('%Y-%m-%d')+"-"+str(uuid.uuid1()) + ".markdown"
    post = open(name,'w')
    post.write("---")
    post.write("\n")
    post.write("layout: post")
    post.write("\n")
    post.write("title: \""+movie['title']+"\"")
    post.write("\n")
    post.write("date:   "+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    post.write("\n")           
    post.write("categories: movie");
    post.write("\n")
    post.write("---")
    post.write("\n")
    
    # content = body.findAll('p')
    # download = body.find('table')

    post.write(doc.prettify())
    post.close()



