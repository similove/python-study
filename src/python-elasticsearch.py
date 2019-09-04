from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

doc = {
    'name': '李四',
    'age': 31,
    'gender': 'female',
    'time': datetime.now()
}

index_res = es.index(index='person1', doc_type='_doc', id=2, body=doc)

print(index_res)

get_res = es.get(index='person1', doc_type='_doc', id=2)

print(get_res)

es.indices.refresh(index='person1')

query_body = {
    'query': {
        'match_all': {}
    }
}
search_res = es.search(index='person1', body=query_body)

print(search_res)
