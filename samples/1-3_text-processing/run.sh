# wget http://www.city.kobe.lg.jp/information/opendata/img/yakei_kobe_20141128.csv

set -x

cat yakei_kobe.csv

cat yakei_kobe.csv | grep 六甲

cat yakei_kobe.csv | cut -d , -f 1,2

cat yakei_kobe.csv | sed 's/,/ /g'

cat yakei_kobe.csv | grep -E '^1'

cat yakei_kobe.csv | grep -E ',.{5},'
