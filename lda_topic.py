#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np
from basic import *
from sklearn.feature_extraction.text import CountVectorizer
import lda
import matplotlib.pyplot as plt
import seaborn as sns


def get_lda_input(chapters):
    corpus = [" ".join(word_list) for word_list in chapters]
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    return X.toarray(), vectorizer


def lda_train(weight, vectorizer):
    model = lda.LDA(n_topics=20, n_iter=1000, random_state=1)
    model.fit(weight)

    doc_num = len(weight)
    topic_word = model.topic_word_
    vocab = vectorizer.get_feature_names()
    titles = ["第{}章".format(i) for i in range(1, doc_num + 1)]

    n_top_words = 20
    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words + 1):-1]
        print('Topic {}: {}'.format(i, ' '.join(topic_words)))

    doc_topic = model.doc_topic_
    print(doc_topic, type(doc_topic))
    plot_topic(doc_topic)
    for i in range(doc_num):
        print("{} (top topic: {})".format(titles[i], np.argsort(doc_topic[i])[:-4:-1]))


def main():
    chapter_list = split_by_chapter("data/芳华-严歌苓.txt")
    chapters = MyChapters(chapter_list)
    weight, vectorizer = get_lda_input(chapters)
    lda_train(weight, vectorizer)


def plot_topic(doc_topic):
    f, ax = plt.subplots(figsize=(10, 4))
    cmap = sns.cubehelix_palette(start=1, rot=3, gamma=0.8, as_cmap=True)
    sns.heatmap(doc_topic, cmap=cmap, linewidths=0.05, ax=ax)
    ax.set_title('proportion per topic in every chapter')
    ax.set_xlabel('topic')
    ax.set_ylabel('chapter')
    plt.show()

    f.savefig('output/topic_heatmap.jpg', bbox_inches='tight')


if __name__ == '__main__':
    main()
