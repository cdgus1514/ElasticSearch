from elasticsearch import Elasticsearch
from elasticsearch import helpers
import pprint as ppr
import json




class ESAPI:

    es = Elasticsearch(hosts="192.168.0.147", port=9200)


    def srvHealthCheck(cls):
        health = cls.es.cluster.health()
        print(health)

    
    def allIndex(cls):
        print(cls.es.cat.indices())

    
    def dataInsert(cls):

        with open("../json_doc_make/tst.json", "r", encoding="utf-8") as fjson:
            data = json.loads(fjson.read())
            
            for n,i in enumerate(data):
                doc = {"cont": i["cont"],
                    "mnagnnm": i["mnagnnm"],
                    "post": i["post"],
                    "rgdt": i["rgdt"],
                    "rgter": i["rgter"],
                    "tel": i["tel"],
                    "title": i["title"]}
                
                res = cls.es.index(index="today191112", doc_type="today", id=n+1, body=doc)
                print(res)


    def searchAll(cls, index=None):

        res = cls.es.search(
            index = "today191112", doc_type = "today",
            body = {
                "query": {"match_all":{}}
            }
        )

        print(json.dumps(res, ensure_ascii=False, indent=4))
    

    def searchFilter(cls):
        
        res = cls.es.search(
            index = "today191112", doc_type = "today", body = {"query": {"match": {"post": "산림교육문화과"}}}
        )

        ppr.pprint(res)

    
    def createIndex(cls):

        cls.es.indices.create(
            index = "today191112",
            body = {
                "settings": {
                    "number_of_shareds": 5
                },
                "mappings": {
                    "today": {
                        "properties": {
                            "cont": {"type": "text"},
                            "mnagnnm": {"type": "text"},
                            "post": {"type": "text"},
                            "rgdt": {"type": "text"},
                            "rgter": {"type": "text"},
                            "tel": {"type": "text"},
                            "title": {"type": "text"}
                        }
                    }
                }
            }
        )
    

ESAPI.allIndex()