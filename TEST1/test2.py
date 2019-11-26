## 엘라스틱서치 인덱스 생성 및 데이터 추가, 확인, 검색

from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch()

doc = {
    "made": "pydole",
    "text": "elasticsearch index test3",
    "timestamp": datetime.now()
}

## 인덱스 생성 & 데이터 넣기
# res = es.index(index="index-test", doc_type="tweet", id=1, body=doc)
# res = es.index(index="index-test", doc_type="tweet", id=2, body=doc)
# res = es.index(index="index-test", doc_type="tweet", id=3, body=doc)
# print(res["result"])



## 데이터 확인
for i in range(1,4):
    res = es.get(index="index-test", doc_type="tweet", id=i)
    print(res["_source"])



## 데이터 검색
es.indices.refresh(index="index-test")
res = es.search(
    index = "index-test",
    body = {
        "query":
            {"match_all":
                {
            }
        }
    }
)

test = list(res['hits']['total'].values())



print("\n\n총 %d 건이 있습니다. " % test[0], end="\n\n")

for hit in res["hits"]["hits"]:
    print("%(timestamp)s %(made)s: %(text)s" % hit["_source"])