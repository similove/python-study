from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

es_client = Elasticsearch()

body = []
for i in range(100):
    for j in range(1000):
        body.append({'index': {'_index': 'person1', '_type': '_doc', '_id': i*100000 + j}})
        body.append({'name': '张'+str(i*100000 + j), 'age': 28, 'gender': 'male'})
    res = es_client.bulk(body=body)
    print(res)
    body.clear()


