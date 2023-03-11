# @Author: zhang
# @time: 2019/7/9 19:10
# @update: 2023/03/11

"""
Function:
    基于tkinter模块
    鲁迅名言查询系统V0.1.0
    Python -V  3.9.1
"""
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from rapidfuzz import fuzz

BASEPATH = os.path.dirname(__file__)


class Window(object):
    '''简单的Window'''

    def __init__(self):
        root = tk.Tk()
        root.minsize(580, 320)  # 窗口大小
        root.resizable(width=False, height=False)   # False窗口大小不可变
        """ iconbitmap 可以设置图标, 需要注意的是不能将 .png .jpg 文件直接修改文件名后缀为 .ico, 需要一些转换工具转换文件 """
        root.iconbitmap(BASEPATH + '\\data\\icon.ico')
        root.title('鲁迅：都是我说的！！')     # 窗口标题

        label1 = Label(text='句子：')    # 标签
        label1.place(x=10, y=10, width=80, height=25)   # 确定位置
        self.line_text = Entry(root)    # 单行文本输入
        self.line_text.place(x=80, y=10, width=300, height=25)
        button = Button(text='开始查询', command=self.inquiry)   # 按钮
        button.place(x=390, y=10, width=60, height=25)

        self.filemenu = tk.StringVar()   # 下拉列表
        self.file_menu = ttk.Combobox(
            root, width=12, textvariable=self.filemenu)
        # 列表内容
        self.file_menu['values'] = ('匹配度: 100%', '匹配度: 90%',
                                    '匹配度: 80%', '匹配度: 70%')
        self.file_menu.place(x=460, y=10, width=100, height=25)
        self.file_menu.current(0)   # 当前显示 100%

        label2 = Label(text='查询结果:')
        label2.place(x=10, y=100, width=80, height=20)
        self.text = Text(root)  # 多行文本显示
        self.text.place(x=80, y=50, width=480, height=240)

        self.paragraphs = self.loadData(BASEPATH + '\\data\\book.txt')   # 数据文件
        root.mainloop()   # 主循环


    def inquiry(self):
        '''查询'''
        sentence = self.line_text.get()   # 获取输入的内容
        matched = []
        score_thresh = self.getScoreThresh()
        self.text.delete(1.0, tk.END)  # 用于删除后续显示的文件
        if not sentence:         # 没有输入句子就查询，会出现弹窗警告
            messagebox.showinfo("Warning", '请先输入需要查询的鲁迅名言')
        else:
            for p in self.paragraphs:
                score = fuzz.partial_ratio(p, sentence)
                if score >= score_thresh and len(sentence) <= len(p):
                    matched.append([score, p])
            infos = []
            # 查找相匹配的内容
            for match in matched:
                infos.append('[匹配度]: %d\n[内容]: %s\n' % (match[0], match[1]))
            if not infos:
                infos.append('未匹配到任何相似度大于或等于%d的句子,请修改匹配度.\n' % score_thresh)
            # 查找到的内容插入文本，并显示
            self.text.insert('insert', '\n\n\n'.join(infos)[:-1])


    def getScoreThresh(self):
        '''根据下拉列表获取匹配度'''
        if self.file_menu.current() == 0:
            return 100
        elif self.file_menu.current() == 1:
            return 90
        elif self.file_menu.current() == 2:
            return 80
        elif self.file_menu.current() == 3:
            return 70


    def loadData(self, data_path):
        '''数据导入'''
        paragraphs = []
        with open(data_path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if line.strip():
                    paragraphs.append(line.strip('\n'))
        return paragraphs


'''运行'''
if __name__ == '__main__':
    Window()
