import sys
import os

import cv2

try:
    cascade_path = sys.argv[1]  # 顔検出用の特徴量ファイルのパス。
    image_path = sys.argv[2]    # 顔を検出する画像ファイルのパス。
except IndexError:
    # コマンドライン引数が足りない場合は使い方を表示して終了する。
    print('Usage: python detect_faces.py CASCADE_PATH IMAGE_PATH', file=sys.stderr)
    exit(1)

# 特徴量ファイルが存在することを確認する。
assert os.path.exists(cascade_path)
# 特徴量ファイルのパスを指定して、分類器オブジェクトを作成する。
classifier = cv2.CascadeClassifier(cascade_path)

# コマンドライン引数で与えたパスの画像ファイルを読み込む。
image = cv2.imread(image_path)
# 顔検出を高速化するため、画像をグレースケールに変換する。
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 顔を検出する。
faces = classifier.detectMultiScale(gray_image)

# 検出された顔のリストについて反復処理する。
# x、y、w、hはそれぞれ検出された顔のX座標、Y座標、幅、高さを表す。
for x, y, w, h in faces:
    # 検出された顔を囲む四角形を描画する。
    cv2.rectangle(image, (x, y), (x + w, y + h), color=(255, 255, 255), thickness=2)

cv2.imwrite('faces.jpg', image)  # 顔検出の結果をfaces.jpgに保存する。

# ウィンドウを表示できない環境では以下のコードはエラーになるが無視して構わない。

cv2.imshow('Faces', image)  # 顔検出の結果をウィンドウに表示する。
cv2.waitKey(0)  # 何かキーが押されたら終了する。
