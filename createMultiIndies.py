from elasticsearch import Elasticsearch
es=Elasticsearch([{"host":"localhost","port":9200}])
print(es.ping())


# create index with sequence 
index_basename="october"
for i in range(2,11):
    response=es.indices.create(index=index_basename+"_"+str(i))
    print(response)
