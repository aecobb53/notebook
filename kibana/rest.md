

https://www.elastic.co/guide/en/elasticsearch/reference/8.0/search-search.html
https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html

Request:
`GET /<target>/_search`
`GET /_search`
`POST /<target>/_search`
`POST /_search`

Where `<target>` is the index you are looking to search in

If both a query and a body parameter are provided, the body is used

Useful `q` parms
size (`int`) `10000`
sort (List[`<field>`:`<direction>`])
_source ?
    _source_excludes ?
    _source_includes ?
stored_fields (List(`str`)) `('*')`
docvalue_fields (List[`str`])
query (Dict)




query:
```json
{
    "query": {
        "bool": {
            "filter": [
                {}
            ],
            "should": [
                {
                    "match_phrase": {
                        "app.name": {
                            "query": "application-name"
                        }
                    }
                }
            ],
            "must": [
                {
                    "match_phrase": {
                        "app.name": {
                            "query": "application-name"
                        }
                    },
                    "query_string": {
                        "query": "message:*",
                        "analize_wildcard": true,
                        "default_filed": "*"
                    },
                    "range": {
                        "@timestamp": {
                            "gte": "2020-01-01T00:00:00.000000Z",
                            "lte": "2020-01-01T00:00:00.000000Z",
                            "format": "date_time"
                        }
                    }
                }
            ],
            "must_not": [
                {
                    "match_phrase": {
                        "app.name": {
                            "query": "application-name"
                        }
                    }
                }
            ],
            "minimum_should_match": 1,

        },
    },
    "docvalue_fields": []
}
```
