# @Author: zhang
# @time: 2019/7/16 10:14
"""
Python      -v 3.7.3
matplotlib  -v 3.1.0
wordcloud   -v 1.5.0

"""

import cv2
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

def plot_word_cloud():
    # 打开文件并读取
    text = open('data.txt','r',encoding='utf-8').read()

    # 读取背景图片,分离色彩，设置图片背景为白色，显示区域为其它颜色
    alice_coloring = cv2.imread('bg.png')
    # 设置词云属性
    wc = WordCloud(background_color='white',   # 背景颜色
                   width=1000,
                   height=600,
                   # 背景图，设置图片背景为白色，显示区域为其它颜色,
                   # 设置为None,绘制一个初始矩形显示
                   mask=alice_coloring,
                   max_font_size=80,  # 最大字体
                   random_state=42,  #
                   max_words=2000,   # 最大单词数
                   font_path='MSYH.TTF')  # 字体

    # 生成词云
    wc.generate(text)

    #
    image_colors = ImageColorGenerator(alice_coloring)

    # 制作显示
    plt.figure()
    plt.imshow(wc)
    plt.axis('off')

    # 保存图片
    # wc.to_file('result.png')

    plt.figure()
    plt.imshow(wc.recolor(color_func=image_colors))
    plt.axis('off')


    # 改变原背景图片颜色
    # plt.figure()
    # plt.imshow(alice_coloring, cmap=plt.cm.gray)
    # plt.axis("off")

    # 屏幕显示
    plt.show()

plot_word_cloud()