#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  elasticsearch import  Elasticsearch 
import io
es=Elasticsearch([{"host":"localhost","port":9200}])
print(es.ping())

with io.open("input.txt","r") as f1:
    data=f1.read()
    f1.close()
data=data.split("\n")

print(data)
for index in data:
    try:
        print(index)
        response=es.indices.delete(index=index)
        print(response)
    except Exception as e:
        print("error occured while creating index "+index+" with the error: "+ str(e))
