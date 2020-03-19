#!/bin/sh

# -r: 再帰的にダウンロードする
# --no-parent: 上のディレクトリを辿らない
# -w 1: リクエスト間のウェイト1秒
# -l 1: リンクをたどるレベル1階層
# -P out: out ディレクトリに出力
# --restrict-file-names=nocontrol: URLエンコードされたパスを保存するときにURLデコードする
#
# ※URLとして /dp を指定すると、--no-parentが思った通りに動かないので、 /dp/ を指定している。
wget -r --no-parent -w 1 -l 1 -P out --restrict-file-names=nocontrol https://gihyo.jp/dp/
