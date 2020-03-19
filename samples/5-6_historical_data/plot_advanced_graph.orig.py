import matplotlib.pyplot as plt

# 第3引数は系列のスタイルを表す文字列を指定する。
# 'b'は青色、'x'はバツ印のマーカー、'-'はマーカーを実線で繋ぐことを意味する。
# キーワード引数labelで系列の名前を指定でき、後述の凡例で使用される。
plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 'bx-', label='1次関数')
# スタイルの'r'は赤色、'o'は丸印のマーカー、'--'は点線を意味する
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'ro--', label='2次関数')
# xlabel()関数でX軸のラベルを指定する
plt.xlabel('Xの値')
# ylabel()関数でY軸のラベルを指定する
plt.ylabel('Yの値')
# title()関数でグラフのタイトルを指定する
plt.title('matplotlibのサンプル')
# lagend()関数で凡例を表示する。loc='best'は最適な位置に表示することを意味する
plt.legend(loc='best')
# X軸の範囲を0〜6とする。ylim()関数で同様にY軸の範囲を指定できる
plt.xlim(0, 6)
# グラフを表示する
plt.show()
