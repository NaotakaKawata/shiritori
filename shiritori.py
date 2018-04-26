# coding: utf-8
import re
import math
import os
import sys
import glob
import random
import re
import pickle

KATAKANA = """アイウエオ
カキクケコ
ガギグゲゴ
サシスセソ
ザジズゼゾ
タチツテト
ダヂズデド
ナニヌネノ
ハヒフヘホ
バビブベボ
パピプペポ
マミムメモ
ラリルレロ
ヤユヨ
ャュョ
ワヲン
"""


def conv_rules_gen():
    inputs = KATAKANA.split('\n')
    title = inputs[0]
    convs = []
    for es in inputs:
        #小文字や長音を変換
        if es == "ヤユヨ" or es == "ワオン" or es == "ャュョ":
            #print(list(map(lambda x: (x[0] + 'ー', x[0] + x[1]), list(zip(es, "アウオ")))))
            convs.append(list(map(lambda x: (x[0] + 'ー', x[0] + x[1]), list(zip(es, "アウオ")))))
        else:
            #print(es)
            convs.append(list(map(lambda x: (x[0] + 'ー', x[0] + x[1]), list(zip(es, title)))))
    return sum(convs, [])


conv_rules = conv_rules_gen()

class Noun(object):
    def __init__(self):
        self.name = ""
        self.orig = ""
        self.yomi = ""
        self.head = ""
        self.tail = ""
        self.head_tail = ""


chain = []
bases = []
nlist = []

for name in glob.glob('./dictionary.txt'):
    allkana = list(map(lambda x: x, KATAKANA.replace('\n', '')))
    for line in open(name).read().split('\n'):
        if line == '': continue
        tp = re.split("[\t|,]",line)
        orig = tp[0]
        yomi = tp[-2]
        for rep in [('ァ', 'ア'), ('ィ', 'イ'), ('ゥ', 'ウ'), ('ェ', 'エ'), ('ォ', 'オ'), ('ャ', 'ヤ'), ('ュ', 'ユ'), ('ョ', 'ヨ'), ('ヴ', 'ウ'), ('ッ', 'ツ'), ('ヅ', 'ツ'), ('ヰ', 'イ'), ('ヱ', 'エ'), ('ヲ', 'オ')]:
            yomi = yomi.replace(rep[0], rep[1])
        for rule in conv_rules:
            yomi = yomi.replace(rule[0], rule[1])

        head = yomi[0]
        tail = yomi[-1]
        #print(orig,yomi)
        n = Noun()
        n.name = name
        n.orig = orig
        n.yomi = yomi
        n.tail = tail
        n.head = head
        n.head_tail = head + tail
        if n.head not in allkana or n.tail not in allkana:
            continue
        if n.tail == 'ン':
            nlist.append(n)
        else:
            bases.append(n)






#語尾の採択確率を設定
def search(tail):
    not_found = True
    if random.random() > 0.98:
        random.shuffle(bases)
    for e, _ in enumerate(bases):
        if tail == n.head and "ン" != n.tail:

        #めんどくさかったので最適なパラメータの値をベタ打ちしています。このままするならパラメータをファイルから読み込む関数を作ってください

            if 'ル' == n.tail and random.random() < 1: continue
            if 'ズ' == n.tail and random.random() < 1 : continue
            if 'ヂ' == n.tail and random.random() < 1 : continue
            if 'ウ' == n.tail and random.random() < 0.9280564666: continue
            if 'ク' == n.tail and random.random() < 0.7121339035877798: continue
            if 'ツ' == n.tail and random.random() < 0.7558545649770779: continue
            if 'プ' == n.tail and random.random() < 0.7425469328280245: continue
            if 'ラ' == n.tail and random.random() < 0.7774023578986695: continue
            if 'リ' == n.tail and random.random() < 0.06087522064859526: continue
            if 'マ' == n.tail and random.random() < 0.40989181282979575: continue
            if 'イ' == n.tail and random.random() < 0.47528551412361997: continue
            if 'ワ' == n.tail and random.random() < 0.24041332419338116: continue
            not_found = False
            break
    if not_found == False:
        t = bases.pop(e)
        return t
    print('最後の単語は、', chain[-1].yomi)
    _ = bases.pop(e)
    point = str(len(chain))

    sys.exit(0)


def main():
    #最初の単語を任意の入力にしたい場合はこっち、引数として任意の単語（カタカナ）を入力
    ini =sys.argv[1]
    orig = ini
    yomi = ini


    for rep in [('ァ', 'ア'), ('ィ', 'イ'), ('ゥ', 'ウ'), ('ェ', 'エ'), ('ォ', 'オ'), ('ャ', 'ヤ'), ('ュ', 'ユ'), ('ョ', 'ヨ'), ('ヴ', 'ウ'), ('ッ', 'ツ'), ('ヅ', 'ツ'), ('ヰ', 'イ'), ('ヱ', 'エ')]:
            yomi = yomi.replace(rep[0], rep[1])
    for rule in conv_rules:
        yomi = yomi.replace(rule[0], rule[1])

    head = yomi[0]
    tail = yomi[-1]
    #print(name, orig, yomi, head, tail)
    k = Noun()
    k.name = name
    k.orig = orig
    k.yomi = yomi
    k.tail = tail
    k.head = head
    k.head_tail = head + tail
    print(1, seed.orig, seed.yomi, seed.tail, seed.head)
    chain.append(k)
    print(1, len(bases),k.orig, k.yomi)
    
    #seed = bases.pop(random.randint(1, len(bases)))
    #chain.append(seed)


    for i in range(100000):
        tail = chain[-1].tail
        t = search(tail)
        chain.append(t)
        print(len(chain), len(bases), t.orig, t.yomi)


if __name__ == '__main__':
    random.shuffle(bases)
    main()
