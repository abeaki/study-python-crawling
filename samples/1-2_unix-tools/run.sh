#!/bin/sh

mkdir -p out

# 書籍の総数を取得
cat in/list.html | grep 'class="totalNum"' | head -n 1 | sed 's/.*（\(.*\)冊）.*/\1/'

# 書籍のリストを取得
cat in/list.html | grep '^\(<h3>\)\?<a href="http://gihyo.jp/book/\d' | sed 's#<a href="\([^"]*\)">\(.*\)</a>.*#\1 \2#' | sed 's#<[^>]*>##g' > out/books.txt

# 著者名を取得
cat in/978-4-7741-5539-5.html | grep 'itemprop="author"' | sed 's/<[^>]*>//g'

# 関連書籍のリストを取得
cat in/978-4-7741-5539-5.html | grep '^<h3><a href="http://gihyo.jp/book/\d' | sed 's#.*href="\(.*\)">\([^<]*\)<.*#\1 \2#' > out/related_books.txt

# イベントレポートの概要を取得
cat in/pycon_apac2013.html | grep '<p class="description">' | sed 's/<[^>]*>//g'

# イベントレポートのリストを取得
cat in/pycon_apac2013.html | sed -n '/<div class="readingContent01">/,/<div  class="pageSwitch01 pageSwitch02">/p' | grep '<li><a href=' | sed 's#.*href="\(.*\)">\([^<]*\)<.*#\1 \2#' > out/event_reports.txt


# https://gihyo.jp/dp/genre/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E3%83%BB%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E9%96%8B%E7%99%BA

# ジャンル内の電子書籍の総数を取得
cat in/genre.html | grep 'class="paging-number"' | grep ' / ' | sed 's#.*/ \([0-9]*\).*#\1#'

# ジャンル内の電子書籍のリストを取得（タイトルのみ）
cat in/genre.html | grep 'itemprop="name"' | sed 's/<[^>]*>//g' | sed 's/^ *//' > out/genre_books.txt


# https://gihyo.jp/dp/ebook/2014/978-4-7741-6759-6

# 電子書籍の価格を取得
cat in/978-4-7741-6759-6.html | grep '<span class="buy">' | sed 's/.*<span class="buy">\(.*\)円.*/\1/'

# 電子書籍の著者名一覧を取得
cat in/978-4-7741-6759-6.html | grep '<aside class="author">' | sed 's#.*<h3>\(.*\)</h3>.*#\1#' | sed 's/<[^>]*>//g'
