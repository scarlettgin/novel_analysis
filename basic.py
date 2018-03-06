#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import jieba
import gensim
import re
jieba.load_userdict("data/person.txt")

STOP_WORDS = set([w.strip() for w in open("data/stopwords.txt").readlines()])


class MyChapters(object):
    def __init__(self, chapter_list):
        self.chapter_list = chapter_list

    def __iter__(self):
        for chapter in self.chapter_list:
            yield cut_words(chapter)


# 过滤词长，过滤停用词，只保留中文
def is_fine_word(word, min_length=2):
    rule = re.compile(r"^[\u4e00-\u9fa5]+$")
    if len(word) >= min_length and word not in STOP_WORDS and re.search(rule, word):
        return True
    else:
        return False


def cut_words(text):
    words = jieba.cut(text)
    fine_words = [w for w in words if is_fine_word(w)]
    return fine_words


def split_by_chapter(filepath):
    text = open(filepath).read()
    chapter_list = re.split(r'第.章\n', text)[1:]
    print(len(chapter_list))
    return chapter_list


def word2vec_train():
    chapters = MyChapters(split_by_chapter(""))
    model = gensim.models.Word2Vec(chapters, size=100, min_count=5, window=5, iter=100)
    model.save("word_vector")


if __name__ == '__main__':
    pass
