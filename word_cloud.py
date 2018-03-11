#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from basic import *
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread
from random import choice


def person_word(name):
    lines = open("data/芳华-严歌苓.txt", "r").readlines()
    word_list = []
    for line in lines:
        if name in line:
            words = cut_words_with_pos(line)
            word_list += words

    cnt = pd.Series(word_list).value_counts()

    return cnt


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return choice(["rgb(94,38,18)", "rgb(128,128,105)", "rgb(39,72,98)"])


def draw_cloud(mask_path, word_freq, save_path):
    mask = imread(mask_path)
    wc = WordCloud(font_path='data/kaiti.TTF',  # 设置字体
                   background_color="black",  # 背景颜色
                   max_words=500,  # 词云显示的最大词数
                   mask=mask,  # 设置背景图片
                   max_font_size=80,  # 字体最大值
                   # random_state=42,
                   )
    wc.generate_from_frequencies(word_freq)

    # show
    image_colors = ImageColorGenerator(mask)
    plt.figure()
    plt.imshow(wc.recolor(color_func=image_colors), interpolation='bilinear')
    plt.axis("off")
    wc.to_file(save_path)
    plt.show()
    return


if __name__ == '__main__':
    # freq = person_word("刘峰")
    # input_freq = freq.to_dict()

    freq = pd.read_csv("data/cnthe.csv", header=None, index_col=0)
    input_freq = freq[1].to_dict()
    draw_cloud("data/he.png", input_freq, "output/hexiaoman.png")

