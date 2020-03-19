import os

from amazon.api import AmazonAPI

# 環境変数から認証情報を読み込む
AMAZON_ACCESS_KEY = os.environ['AMAZON_ACCESS_KEY']
AMAZON_SECRET_KEY = os.environ['AMAZON_SECRET_KEY']
AMAZON_ASSOCIATE_TAG = os.environ['AMAZON_ASSOCIATE_TAG']

# AmazonAPIオブジェクトを作成する
# RegionパラメータでAmazon.co.jpを選択する
amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOCIATE_TAG, Region='JP')

# Keywordsに指定した語句にマッチする商品を検索する
# SearchIndex='All'はすべてのカテゴリから検索することを意味する
products = amazon.search(Keywords='kindle', SearchIndex='All')

# 得られた商品について反復する
for product in products:
    print(product.title)      # 商品名
    print(product.offer_url)  # 商品のURL
    price, currency = product.price_and_currency
    print(price, currency)    # 価格と通貨
    print(product.get_attribute('ProductGroup'))
