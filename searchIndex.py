#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from elasticsearch import Elasticsearch 
es=Elasticsearch([{"host":"localhost","port":9200}])

print(es.ping())


index="oct*"
try:
    response=es.search(index=index)
    print(response["_shards"]["total"])
except Exception as e:
    print(str(e))
