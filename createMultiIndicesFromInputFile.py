from elasticsearch import Elasticsearch
es=Elasticsearch([{"host":"localhost","port":9200}])
print(es.ping())

import io

with io.open("input.txt","r",encoding="utf-8") as f1:
    data=f1.read()
    f1.close
data=data.split("\n")
print(data)


for index in data:
    response=es.indices.create(index=index)
    print(response)
