rm -r gihyo.jp
wget -r --no-parent -w 1 -l 1 --restrict-file-names=nocontrol -I /dp/ebook/,/dp/assets/ https://gihyo.jp/dp/
#wget -w 1 -p https://gihyo.jp/dp/

wget -r https://gihyo.jp/dp/assets/style/parts0711.png
wget -r https://gihyo.jp/dp/assets/style/parts0711_small.png
wget -r https://gihyo.jp/dp/assets/style/wait.gif
wget -r https://gihyo.jp/assets/images/dummy.png
