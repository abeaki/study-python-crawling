
### Setup

```
$ gcloud auth login
$ gcloud config set project ***
```

```
$ bq mk twitter
Dataset 'cp100-trial:twitter' successfully created.
$ bq mk twitter.tweets id:string,lang:string,screen_name:string,text:string,created_at:timestamp
Table 'cp100-trial:twitter.tweets' successfully created.
$ bq show twitter.tweets
Table cp100-trial:twitter.tweets

   Last modified             Schema            Total Rows   Total Bytes   Expiration
 ----------------- -------------------------- ------------ ------------- ------------
  29 Aug 16:57:18   |- id: string              0            0
                    |- lang: string
                    |- screen_name: string
                    |- text: string
                    |- created_at: timestamp
```


### Run


```
$ forego run python import_from_stream_api_to_bigquery.py
$ bq query 'SELECT lang, COUNT(lang) AS count FROM twitter.tweets GROUP BY lang ORDER BY count DESC LIMIT 20'
Waiting on bqjob_r6bf27f4e434c00d9_0000014f78ad94c6_1 ... (0s) Current status: RWaiting on bqjob_r6bf27f4e434c00d9_0000014f78ad94c6_1 ... (1s) Current status: RWaiting on bqjob_r6bf27f4e434c00d9_0000014f78ad94c6_1 ... (1s) Current status: DONE
+------+-------+
| lang | count |
+------+-------+
| ja   |   298 |
| en   |   290 |
| ar   |    67 |
| es   |    57 |
| in   |    46 |
| und  |    43 |
| tl   |    32 |
| ko   |    31 |
| fr   |    26 |
| ru   |    24 |
| tr   |    23 |
| th   |    19 |
| de   |     9 |
| pt   |     8 |
| it   |     5 |
| pl   |     3 |
| nl   |     2 |
| el   |     2 |
| vi   |     2 |
| no   |     2 |
+------+-------+
$ bq query 'SELECT INTEGER(ROUND(LENGTH(text), -1)) AS length, COUNT(*) AS count FROM twitter.tweets GROUP BY length ORDER BY length DESC'
Waiting on bqjob_r35fefdcf724f1a20_0000014f78bbf7e2_1 ... (0s) Current status: RWaiting on bqjob_r35fefdcf724f1a20_0000014f78bbf7e2_1 ... (0s) Current status: DONE
+--------+-------+
| length | count |
+--------+-------+
|    150 |     2 |
|    140 |   154 |
|    130 |    48 |
|    120 |    46 |
|    110 |    50 |
|    100 |    53 |
|     90 |    62 |
|     80 |    59 |
|     70 |    60 |
|     60 |    77 |
|     50 |    80 |
|     40 |    75 |
|     30 |   101 |
|     20 |    86 |
|     10 |    44 |
|      0 |     3 |
+--------+-------+
```

本当ならROUNDではなくCEILのほうがわかりやすいけど、CEILには第2引数が指定できない。
140を超えているのは、HTMLエスケープされているため。
