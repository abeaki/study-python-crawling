# -*- coding: utf-8 -*-
# 日本語で検索したい場合は上のタグを入れる

from gdata import *
import gdata.youtube
import gdata.youtube.service

search_word = "犬" # 犬の動画を検索
client = gdata.youtube.service.YouTubeService()

# サーチクエリを作成
query = gdata.youtube.service.YouTubeVideoQuery()
query.vq = search_word # 検索ワード
query.start_index = 1 # 何番目の動画から検索するか
query.max_results = 10 # いくつの動画情報を取得したいか
query.racy = "exclude" # 最後の動画を含めるか
query.orderby = "relevance" # どんな並び順にするか

# 検索を実行し、feedに結果を入れる
feed = client.YouTubeQuery(query)

for entry in feed.entry:
    # 動画のリンクを取り出す
    # LinkFinderは、
    #   from gdata import *
    # から使用
    link = LinkFinder.GetHtmlLink(entry)
    print link
