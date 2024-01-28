#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from elasticsearch import Elasticsearch



es=Elasticsearch([{"host":"localhost","port":9200}])

#print(es.__version__)

print(es.ping())

es.indices.create(index="second-index-2024-01-28")
