Name

しりとりプログラム
====

## Overview

最長しりとり問題に取り組んでいる。

read_file.pyはしりとりプログラムで、bayes_optim.pyはパラメータ最適化に使用している。

ここでいうパラメータは「しりとりの語尾の出現確率」を表す。

## Description

一般的に最長しりとり問題はNP困難であるため、そのまま最適解を計算することは難しい。

そこで今回は計算量を減らすことを目的としランダムである程度までしりとりを続けてみた。

こちらは毎日新聞のコーパスから単語を抽出した単語の語頭と語尾の分布を調べた結果だが、このように偏りが存在する。

偏りが存在すると語頭の在庫がなくなると語尾でその単語がでてしまうと在庫がないためしりとりを続けられないとう問題がある。

ベイズ最適化を用いてパラメータを最適化している。



## Usagebase
最適化する場合
~~~
$python bayes_optim.py
~~~
パラメータが分かった後
~~~
$python3 read_file.py
~~~
## Install
~~~
pip install bayesian-optimization
~~~


## Author

[kawata](https://github.com/NaotakaKawata)
