# -*- coding:utf-8 -*-
import jieba.analyse as analyse

s = open('word/中国移动广东公司业务通则V2.0.txt','r',encoding='utf8').read()
tags=analyse.extract_tags(s,topK=500,withWeight=False, allowPOS=())
f1 = open('word/训练TF-IDF.txt','w')
for line in tags:
    f1.write(line+'\n')
f1.close()

f="\n".join(analyse.textrank(s,topK=500))
f2 = open('word/训练textrank.txt','w')
f2.write(str(f))