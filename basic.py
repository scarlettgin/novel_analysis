#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import jieba
import pandas
from sklearn.feature_extraction.text import CountVectorizer
import gensim
import lda
import re

STOP_WORDS = set(open("data/stopwords.txt").readlines())


class MyChapters(object):
    def __init__(self, chapter_list):
        self.chapter_list = chapter_list

    def __iter__(self):
        for chapter in self.chapter_list:
            yield cut_words(chapter)


# 只保留中文
def isAllChinese(line):
    rule = re.compile(r"^[\u4e00-\u9fa5]+$")
    res = re.search(rule, line)
    if res:
        return True
    else:
        return False


def cut_words(text):
    words = jieba.cut(text)
    filter_words = [w for w in words if w not in STOP_WORDS and len(w) > 1 and isAllChinese(w)]
    return filter_words


def split_by_chapter():
    text = open("").read()
    chapter_list = re.split(r'第.章\n', text)
    print(len(chapter_list))
    return chapter_list


def word2vec_train():
    chapters = MyChapters(split_by_chapter())
    model = gensim.models.Word2Vec(chapters, size=100, min_count=5, window=5, iter=100)
    model.save("word_vector")


def get_lda_corpus():
    vectorizer = CountVectorizer()

    return


def lda_train():
    model = lda.LDA(n_topics=2, n_iter=500, random_state=1)
    return


def word_cloud():
    return


def gen_ciku():
    return


if __name__ == '__main__':
    print(isAllChinese('faiuehf000(((<<,,我的'))
