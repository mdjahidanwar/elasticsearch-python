#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from elasticsearch import Elasticsearch 
es=Elasticsearch([{"host":"localhost","port":9200}])

print(es.ping())

##indices="october*"
##index="october"
##for i in range(2,10):
##    response=es.indices.create(index+"_"+str(i))
##    print(response)
##    print(es.search(index=indices))


## search and display the index names based on the given search pattern
index_pattern="october_*"
response=es.indices.get_alias(index_pattern)

if(len(response)>0):
    for index in response:
        response=es.indices.delete(index)
        print(response)
else:
    print("no index found on the given pattern")
