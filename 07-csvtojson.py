#!/usr/bin/python
# coding: utf-8

import csv
import json

data=[]

with open('file.csv') as f:
 for line in csv.DictReader(f):
  line_json=json.dumps(line)
  data.append(line_json)
print(data)


