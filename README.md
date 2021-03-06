

しりとりプログラム
====

## Overview

最長しりとり問題に取り組んでいる。

主にこちらを参考にさせていただきました。ぜひこちらも見てください。

http://catindog.hatenablog.com/entry/2017/01/19/214348

read_file.pyはしりとりプログラムで、bayes_optim.pyはパラメータ最適化に使用している。

ここでいうパラメータは「しりとりの語尾の出現確率」を表す。


## Description

一般的に最長しりとり問題はNP困難であるため、そのまま最適解を計算することは難しい。

そこで今回は計算量を減らすことを目的としランダムである程度までしりとりを続けてみた。

こちらは毎日新聞のコーパスから単語を抽出した単語の語頭と語尾の分布を調べた結果だが、このように偏りが存在する。


![語頭](https://github.com/NaotakaKawata/shiritori/blob/master/images/goto.png)

![語尾](https://github.com/NaotakaKawata/shiritori/blob/master/images/gobi.png)

偏りが存在すると語頭の在庫がなくなると語尾でその単語がでてしまうと在庫がないためしりとりを続けられないとう問題がある。

ベイズ最適化を用いてパラメータを最適化している。



## Usagebase

まず同ディレクトリにしりとりで使用したい文書をMecabにかけたものをdictionary.txtとして保存してください。

最適化する場合
~~~
$python bayes_optim.py
~~~
パラメータが分かった後,shiritori.pyの108～116行目の値を、result.txtで出力された値に書き換える。

例：x0がウ、x1がクの出現確率に当たる
~~~
$python3 shiritori.py
~~~
## Install
~~~
pip install bayesian-optimization
~~~


## Author

[kawata](https://github.com/NaotakaKawata)
