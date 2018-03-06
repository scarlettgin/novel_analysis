#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np
from basic import *
from sklearn.feature_extraction.text import CountVectorizer
import lda


# http://blog.csdn.net/real_myth/article/details/51239847
def get_lda_input(chapters):
    corpus = [" ".join(word_list) for word_list in chapters]
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    return X.toarray(), vectorizer


def lda_train(weight, vectorizer):
    model = lda.LDA(n_topics=10, n_iter=500, random_state=1)
    model.fit(weight)

    doc_num = len(weight)
    topic_word = model.topic_word_
    vocab = vectorizer.get_feature_names()
    titles = ["第{}章".format(i) for i in range(1, doc_num + 1)]

    n_top_words = 8
    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words + 1):-1]
        print('Topic {}: {}'.format(i, ' '.join(topic_words)))

    doc_topic = model.doc_topic_
    for i in range(doc_num):
        print("{} (top topic: {})".format(titles[i], doc_topic[i].argmax()))


def main():
    chapter_list = split_by_chapter("data/test")
    chapters = MyChapters(chapter_list)
    weight, vectorizer = get_lda_input(chapters)
    lda_train(weight, vectorizer)


if __name__ == '__main__':
    main()