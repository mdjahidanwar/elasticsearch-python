from elasticsearch import Elasticsearch



es=Elasticsearch([{"host":"localhost","port":9200}])


print(es.ping())

indices=es.indices.get_alias("*")


for index in indices:
    print(indices)
