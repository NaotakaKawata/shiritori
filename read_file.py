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
    ps = list(map(float, sys.argv[1:]))
    not_found = True
    if random.random() > 0.98:
        random.shuffle(bases)
    for e, _ in enumerate(bases):
        n = bases[e]
        if tail == n.head and "ン" != n.tail:

            if 'ル' == n.tail and random.random() < 1: continue
            if 'ズ' == n.tail and random.random() < 1 : continue
            if 'ヂ' == n.tail and random.random() < 1 : continue
            if 'ウ' == n.tail and random.random() < ps[0]: continue
            if 'ク' == n.tail and random.random() < ps[1]: continue
            if 'ツ' == n.tail and random.random() < ps[2]: continue
            if 'プ' == n.tail and random.random() < ps[3]: continue
            if 'ラ' == n.tail and random.random() < ps[4]: continue
            if 'リ' == n.tail and random.random() < ps[5]: continue
            if 'マ' == n.tail and random.random() < ps[6]: continue
            if 'イ' == n.tail and random.random() < ps[7]: continue
            if 'ワ' == n.tail and random.random() < ps[8]: continue
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

    seed = bases.pop(random.randint(1, len(bases)))
    chain.append(seed)
    print(1, seed.orig, seed.yomi, seed.tail, seed.head)

    for i in range(100000):
        tail = chain[-1].tail
        t = search(tail)
        chain.append(t)
        print(len(chain), len(bases), t.orig, t.yomi)


if __name__ == '__main__':
    random.shuffle(bases)
    main()
