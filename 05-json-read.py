#!/usr/bin/python
# coding: utf-8

import json
#JSON ファイルの読み込み
f = open('test.json', 'r')
json_dict = json.load(f)
#print('json_dict:{}'.format(type(json_dict)))
#print json_dict["book1"]
#book-page=json_dict["book1"]["page"]
#print "page is" +  book-page
print '{book_title} is {book_page} page'.format(book_title=json_dict["book1"]["title"],book_page=json_dict["book1"]["page"])
#print '%(book1)s is' %json_dict
