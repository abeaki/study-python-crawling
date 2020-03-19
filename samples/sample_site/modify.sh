set -x

rm -r sample.scraping-book.com
cp -R gihyo.jp sample.scraping-book.com

BOOK_NAME="Pythonクローリング＆スクレイピング -データ収集・解析のための実践開発ガイド-"
BOOK_SHORT_NAME="Scraping-Book"

# * titleを変更
# * meta descriptionを変更
# * meta keywordsを削除
# * OPDS Catalogへのlinkを削除
# * apple-touch-icon-precomposedへのlinkを削除
# * twitter cardのmetaを削除
# * ogpのmetaを削除
# * facebookのmetaを削除
# * 1行のscriptを削除
# * 複数行のscriptを削除
# * meta robotsを追加
# * IE向け条件付きコメントを削除
# * home-titleを変更
# * home-subtitleを変更
# * 使用できないリンクのtitleを変更
# * 定期購読のためのリンクにtitleを追加
# * Twitterアカウントへのリンクを削除
# * このサイトについてのリンクを変更
# * ヘルプへのリンクを削除
# * サンプルである旨を明記
# 以下詳細ページのみ対象
# * 紙の書籍へのリンクを削除
# * 購入できない旨を追記
# * 学校・法人等団体でのご利用についてを削除
# * 発売日に通知するリンクを削除
# * SNSのボタンを削除
# * 書籍内のキーワード検索を利用できないことを明記
LANG=C find sample.scraping-book.com -name 'assets' -prune -or -type f -exec sed -E -i '' \
	-e "s/Gihyo Digital Publishing … 技術評論社の電子書籍/$BOOK_NAME サンプルページ/" \
	-e "s/技術評論社の電子書籍（電子出版）販売サイト/$BOOK_NAME サンプルページ/" \
	-e '/<meta name="keywords"/d' \
	-e '/<link rel="related"/d' \
	-e '/<link rel="apple-touch-icon-precomposed"/d' \
	-e '/<meta name="twitter:/d' \
	-e '/<meta property="og:/d' \
	-e '/<meta property="fb:/d' \
	-e '/<script.*<\/script>/d' \
	-e '/<script>/,/<\/script>/d' \
	-e 's|<!--\[if lt IE 9\]>|<meta name="robots" content="noindex,noarchive"/>|' \
	-e '/<!\[endif\]-->/d' \
	-e '/<!--\[if .*>/d' \
	-e "s/Gihyo Digital Publishing/$BOOK_SHORT_NAME/g" \
	-e 's|<h2 class="home-subtitle">.*</h2>|<h2 class="home-subtitle">これは書籍用のサンプルページです。購入などの操作はできません。</h2>|' \
	-e 's/title="(ログイン・会員登録|カートは空です|(次|前)の(ページ|バナー)|ストア|マイページ|お知らせ|ヘルプ|定期購読を申し込む|カートに入れる|ギフトコードを購入)"/title="サンプルページのため利用できません"/g' \
	-e 's|<a href="/dp/subscription">|<a href="/dp/subscription" title="サンプルページのため利用できません">|' \
	-e '/<li>Twitter:/d' \
	-e 's|/dp/help/about/site|/|' \
	-e '/<li><a href="\/dp\/help\/about\//d' \
	-e "s|<p id=\"storeCopyright\"><small>|<p id=\"storeCopyright\"><span style=\"color:red;font-size:1.8em;\">このページは「${BOOK_NAME}」のためのサンプルサイトです。特別の許可を得て技術評論社の著作物を使用しています。</span><br/><small>|" \
	-e 's|<li>本書は，<a href=.*</li>|<li>これは書籍サンプルのページです。</li>|' \
	-e 's|<li class="need-login">.*</li>|<li class="need-login">サンプルサイトなので購入はできません。</li>|' \
	-e '/<li class="corporate">.*<\/li>/d' \
	-e 's|<a href="#" id="releaseNotify".*</a>||' \
	-e 's@<li class="(twitter|facebook|gplus|hatena)">.*</li>@<li></li>@' \
	-e 's/(本書内を検索するキーワードを入力|本書内のキーワード)/利用できません/g' \
	{} \;

# additionの中身で上書き
rsync --exclude='*.swp' -a addition/ sample.scraping-book.com/

# CSSの色を置き換える
# * 濃い青
# * 薄めの青
# * 濃い青その2
# * 緑
# * 非常に薄い青
# * 赤
# * 非常に薄い青（透過あり）
sed -E -i '' \
	-e 's/#0068b6/#E36409/g' \
	-e 's/#4d95cc/#FF973C/g' \
	-e 's/#1a77bd/#E36409/g' \
	-e 's/#128912/#D109E3/g' \
	-e 's/#ebf4fd/#FFFFD5/g' \
	-e 's/#de3434/#11CCCC/g' \
	-e 's/rgba\(235,244,253,0\.9\)/#FFFFD5/g' \
	sample.scraping-book.com/dp/assets/style/*.css

# CSSスプライトを変換する
# * 色を反転する
# * 「PayPalへ接続中」を削除
# * 画像のロゴを書き換える
convert gihyo.jp/dp/assets/style/parts0711.png \
	-negate \
	-fill black -draw 'rectangle 0,256 552,358' \
	-draw 'rectangle 278,216 552,358' \
	-fuzz 0% -fill none -floodfill +0+256 black \
	-fill '#FD9752' -font "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc" -gravity north-west \
	-pointsize 26 -annotate +0+256 "Pythonクローリング＆スクレイピング\nサンプルサイト" \
	-pointsize 25 -annotate +0+308 "サン\nプル" \
	-strip \
	sample.scraping-book.com/dp/assets/style/parts0711.png

convert sample.scraping-book.com/dp/assets/style/parts0711.png \
	-resize 50% -strip sample.scraping-book.com/dp/assets/style/parts0711_small.png

cat addition/.htaccess secrets/.htaccess > sample.scraping-book.com/.htaccess
cp secrets/.htpasswd sample.scraping-book.com/

#chmod -R o+r sample.scraping-book.com
#open sample.scraping-book.com/dp/assets/style/parts0711.png
