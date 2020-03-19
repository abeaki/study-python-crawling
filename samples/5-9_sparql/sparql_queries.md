Endpoint: http://ja.dbpedia.org/sparql

### 1. 東京都の全属性

```
SELECT * WHERE {
    <http://ja.dbpedia.org/resource/東京都> ?p ?o .
}
```

### 2. 東京都の全属性 (PREFIXを使用)

```
SELECT * WHERE {
    dbpedia-ja:東京都 ?p ?o .
}
```

### 3. 美術館の一覧

```
SELECT * WHERE {
    ?s rdf:type schema:Museum .
} ORDER BY ?s
```

### 4. 美術館の個数

```
SELECT COUNT(*) WHERE {
    ?s rdf:type schema:Museum .
}
```

-> 1879

### 5. 日本の美術館の一覧

```
SELECT * WHERE {
    ?s rdf:type schema:Museum .
    ?s dbpedia-owl:location ?location .
    ?location dbpedia-owl:country dbpedia-ja:日本 .
} ORDER BY ?s
```

### 6. 日本の美術館の一覧 (セミコロンを使用)

```
SELECT * WHERE {
    ?s rdf:type schema:Museum ;
       dbpedia-owl:location ?location .
    ?location dbpedia-owl:country dbpedia-ja:日本 .
} ORDER BY ?s
```

### 日本の美術館の一覧 (所在地を表示)

```
SELECT * WHERE {
    ?s rdf:type schema:Museum .
    ?s prop-ja:所在地 ?address .
} ORDER BY ?s
```

### 日本の美術館の一覧 (所在地を表示+セミコロン)

```
SELECT * WHERE {
    ?s rdf:type schema:Museum ;
       prop-ja:所在地 ?address .
} ORDER BY ?s
```

### 日本の美術館の一覧 (FILTER使用)

```
SELECT * WHERE {
    ?s rdf:type schema:Museum ;
       prop-ja:所在地 ?address .
    FILTER REGEX(?address, "^\\p{Han}{2,3}[都道府県]")
} ORDER BY ?s
```

### 日本の美術館の一覧 (位置情報付き)

```
SELECT * WHERE {
    ?s rdf:type schema:Museum ;
       prop-ja:所在地 ?address .
    FILTER REGEX(?address, "^\\p{Han}{2,3}[都道府県]")
    OPTIONAL {
       ?s prop-ja:経度度 ?lon_degree ;
          prop-ja:経度分 ?lon_minute ;
          prop-ja:経度秒 ?lon_second ;
          prop-ja:緯度度 ?lat_degree ;
          prop-ja:緯度分 ?lat_minute ;
          prop-ja:緯度秒 ?lat_second .
    }
} ORDER BY ?s
```

### 日本の美術館の一覧 (ラベル, 位置情報付き)

```
SELECT * WHERE {
    ?s rdf:type schema:Museum ;
       prop-ja:所在地 ?address .
    FILTER REGEX(?address, "^\\p{Han}{2,3}[都道府県]")
    OPTIONAL { ?s rdfs:label ?label } .
    OPTIONAL {
       ?s prop-ja:経度度 ?lon_degree ;
          prop-ja:経度分 ?lon_minute ;
          prop-ja:経度秒 ?lon_second ;
          prop-ja:緯度度 ?lat_degree ;
          prop-ja:緯度分 ?lat_minute ;
          prop-ja:緯度秒 ?lat_second .
    }
} ORDER BY ?s
```

### 7. 日本の美術館の個数

```
SELECT COUNT(*) WHERE {
    ?s rdf:type schema:Museum ;
       dbpedia-owl:location ?location .
    ?location dbpedia-owl:country dbpedia-ja:日本 .
}
```

-> 666

### 8. 日本の美術館の一覧 (位置情報付き)

```
SELECT * WHERE {
    ?s rdf:type schema:Museum ;
       prop-ja:経度度 ?lon_degree ;
       prop-ja:経度分 ?lon_minute ;
       prop-ja:経度秒 ?lon_second ;
       prop-ja:緯度度 ?lat_degree ;
       prop-ja:緯度分 ?lat_minute ;
       prop-ja:緯度秒 ?lat_second ;
       dbpedia-owl:location ?location .
    ?location dbpedia-owl:country dbpedia-ja:日本 .
} ORDER BY ?s
```

### 9. 日本の美術館の個数 (位置情報付き)

```
SELECT COUNT(*) WHERE {
    ?s rdf:type schema:Museum ;
       prop-ja:経度度 ?lon_degree ;
       prop-ja:経度分 ?lon_minute ;
       prop-ja:経度秒 ?lon_second ;
       prop-ja:緯度度 ?lat_degree ;
       prop-ja:緯度分 ?lat_minute ;
       prop-ja:緯度秒 ?lat_second ;
       dbpedia-owl:location ?location .
    ?location dbpedia-owl:country dbpedia-ja:日本 .
}
```

-> 214

### 10. 日本の美術館の一覧 (位置情報はオプショナル)

```
SELECT * WHERE {
    ?s rdf:type schema:Museum ;
       dbpedia-owl:location ?location .
    ?location dbpedia-owl:country dbpedia-ja:日本 .
    OPTIONAL {
       ?s prop-ja:経度度 ?lon_degree ;
          prop-ja:経度分 ?lon_minute ;
          prop-ja:経度秒 ?lon_second ;
          prop-ja:緯度度 ?lat_degree ;
          prop-ja:緯度分 ?lat_minute ;
          prop-ja:緯度秒 ?lat_second .
    } .
} ORDER BY ?s
```

### 11. 日本の美術館の一覧 (ラベル、住所、位置情報はオプショナル)

```
SELECT * WHERE {
    ?s rdf:type schema:Museum ;
       dbpedia-owl:location ?location .
    ?location dbpedia-owl:country dbpedia-ja:日本 .
    OPTIONAL { ?s rdfs:label ?label } .
    OPTIONAL { ?s prop-ja:所在地 ?address } .
    OPTIONAL {
       ?s prop-ja:経度度 ?lon_degree ;
          prop-ja:経度分 ?lon_minute ;
          prop-ja:経度秒 ?lon_second ;
          prop-ja:緯度度 ?lat_degree ;
          prop-ja:緯度分 ?lat_minute ;
          prop-ja:緯度秒 ?lat_second .
    } .
} ORDER BY ?s
```

### 12. 日本の美術館の一覧 (住所は一つだけ取得)

```
SELECT ?s, ?label, SAMPLE(?address) AS ?address, ?lon_degree, ?lon_minute, ?lon_second, ?lat_degree, ?lat_minute, ?lat_second WHERE {
    ?s rdf:type schema:Museum ;
       dbpedia-owl:location ?location .
    ?location dbpedia-owl:country dbpedia-ja:日本 .
    OPTIONAL { ?s rdfs:label ?label } .
    OPTIONAL { ?s prop-ja:所在地 ?address } .
    OPTIONAL {
       ?s prop-ja:経度度 ?lon_degree ;
          prop-ja:経度分 ?lon_minute ;
          prop-ja:経度秒 ?lon_second ;
          prop-ja:緯度度 ?lat_degree ;
          prop-ja:緯度分 ?lat_minute ;
          prop-ja:緯度秒 ?lat_second .
    } .
} ORDER BY ?s
```
