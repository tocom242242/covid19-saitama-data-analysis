# 埼玉のCOVID-19（コロナウイルス）に関するデータと分析

埼玉県が公開しているデータを使って埼玉県のCOVID-19のデータ分析を行っています。

少しずつグラフなどは追加していきます。

main.ipynb に手法なプログラムを記述していく予定です。

## main.ipynbの動かし方

1. 埼玉県のオープンデータが公開されている[ページ](https://opendata.pref.saitama.lg.jp/data/dataset/covid19-jokyo)からcsvデータをダウンロードします

2. main.ipynbの最初のセルでデータを読み込むコードがあるので、ダウンロードしたファイルのpathに書き直してください

3. 後はmain.ipynbを実行することでグラフが出力されます。

## 作成したグラフ

main.ipynbで作成したグラフは以下のようになります。

#### 埼玉県の陽性者数の推移
![各市町村の陽性者数](https://github.com/tocom242242/covid19-saitama-data-analysis/blob/master/figs/yousei_num.png)

#### 各市町村の陽性者数
![埼玉県の陽性者数の推移](https://github.com/tocom242242/covid19-saitama-data-analysis/blob/master/figs/yousei_num_by_each_city.png)

#### 各市町村の陽性者数の推移
![各市町村の陽性者数の推移](https://github.com/tocom242242/covid19-saitama-data-analysis/blob/master/figs/yousei_num_time_series_by_each_city.png)

#### 各市町村の陽性者数の推移の相関
![各市町村の陽性者数の推移](https://github.com/tocom242242/covid19-saitama-data-analysis/blob/master/figs/city_corr.png)


## 参考文献
1. [【埼玉県】新型コロナウイルス感染症の発生状況](https://opendata.pref.saitama.lg.jp/data/dataset/covid19-jokyo)
1. [新型コロナウイルス感染症の埼玉県内の発生状況](https://www.pref.saitama.lg.jp/a0701/covid19/jokyo.html)
