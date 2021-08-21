"""
A tool to download music with mxget and tkinter

# Date: 2021/05/17
# Author: zhangsh
# Version: v1.1

# 1. 不要下载完成插入信息，在显示歌曲列表的下方新建输出窗口， 输出每条下载完成信息

"""

import os
import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askdirectory

BASE_DIR = os.path.dirname(__file__)


class Application(object):

    def __init__(self):
        root = tk.Tk()
        root.minsize(620, 610)  # 窗口大小
        root.resizable(width=False, height=False)  # False 窗口大小不可变
        root.iconbitmap(BASE_DIR + '/mico.ico')  # 图标
        root.title('Tk!')  # 窗口标题
        # root['bg'] = '#272822'  # 窗口背景颜色
        # row 1
        song_title_label = tk.Label(text='Song Title')  # 第一行标签提示
        song_title_label.place(x=10, y=10, width=80, height=30)  # 确定位置

        self.input_song_title = tk.Entry(root)  # 单行文本输入，输入歌曲名
        self.input_song_title.place(x=100, y=10, width=400, height=30)

        query_btn = tk.Button(text='Search', command=self.inquiry)  # 搜索歌曲按钮
        query_btn.place(x=510, y=10, width=80, height=30)
        # row 2
        song_list_label = tk.Label(text='Songs List')  # 第二行提示标签
        song_list_label.place(x=10, y=160, width=80, height=30)
        self.show_song_list = tk.Text(root, font='14', state='disabled')  # 多行文本显示搜索到的歌曲
        self.show_song_list.place(x=100, y=50, width=490, height=310)

        song_list_label = tk.Label(text='Download')  # 标签
        song_list_label.place(x=10, y=410, width=80, height=30)
        self.show_down_msg = tk.Text(root, font='14', state='disabled')  # 多行文本显示下载完成
        self.show_down_msg.place(x=100, y=370, width=490, height=110)
        # row 3
        combostyle = ttk.Style()  # 定义 ttk 风格
        combostyle.theme_create('combostyle', parent='alt',
                                settings={'TCombobox': {'configure': {
                                    'foreground': '#000',  # 字体颜色
                                    'selectforeground': '#000',  # 选择后的字体颜色
                                    'selectbackground': '#fff',  # 选择后的背景颜色
                                    'fieldbackground': '#fff',  # 下拉框颜色
                                    'background': '#fff',  # 背景颜色
                                    "font": 10,  # 字体大小
                                    "font-weight": "bold"
                                }}}
                                )
        combostyle.theme_use('combostyle')
        self.song_id_list_ = tk.StringVar()
        self.song_id_list = ttk.Combobox(root, width=12, textvariable=self.song_id_list_, justify='center',
                                         state='readonly')  # 歌曲 id 下拉列表
        self.song_id_list['values'] = ['01', '02', '03', '04', '05', '06', '07', '08', '09']  # 下拉列表 id
        self.song_id_list.place(x=100, y=500, width=60, height=30)
        self.song_id_list.current(0)  # 下拉列表取默认值第一个 01

        self.is_download_lyric = tk.BooleanVar()
        download_lyric_btn = tk.Checkbutton(root, text='Download Lyric', variable=self.is_download_lyric,
                                            relief='ridge', onvalue=True, offvalue=False)  # 是否选择歌词 checkbox
        download_lyric_btn.place(x=210, y=500, width=140, height=30)
        # row 4
        default_save_to = (os.path.expanduser('~')+'\\Downloads').replace('\\', '/')
        self.save_path = tk.StringVar()  # 设置下载歌曲的位置参数
        self.save_path.set(default_save_to)
        os.system(r'mxget config --dir '+default_save_to)

        select_path_btn = tk.Button(root, text="Select Path", command=self.select_download_path)  # 选择下载歌曲的按钮
        select_path_btn.place(x=100, y=535, width=100, height=30)

        show_path = tk.Entry(root, textvariable=self.save_path, state='disable', disabledforeground='#000',
                             disabledbackground='#fff')  # 显示选择下载歌曲的位置
        show_path.place(x=210, y=535, width=400, height=30)
        # row 5
        download_btn = tk.Button(text='Download', command=self.download)  # 下载歌曲按钮
        download_btn.place(x=100, y=570, width=100, height=30)

        self.song_id_dict = {}  # 歌曲编号与对应的 id
        self.song_name_dict = {}  # 歌曲编号与对应的 name
        root.mainloop()  # 主循环

    def select_download_path(self):
        """ 选择下载路径 """
        path = askdirectory()
        if path:
            self.save_path.set(path)
            os.system(f'mxget config --dir {path}')

    def inquiry(self):
        """ 查询关键词歌曲 """
        self.show_song_list['state'] = 'normal'
        song_title = self.input_song_title.get()  # 获取输入的歌曲名
        if not song_title:  # 没有输入歌名就查询，会出现弹窗警告
            messagebox.showinfo("Warning", 'Please input song title...')
        else:
            self.show_song_list.delete(1.0, tk.END)  # 用于删除后续显示的歌曲列表信息
            try:
                songs_data = subprocess.run(f'mxget search -k "{song_title}"',stdout=subprocess.PIPE, encoding='utf8')
            except Exception as e:
                self.show_song_list.insert('insert', f'\n Not found songs about {song_title}...')
                return
            if songs_data:
                songs_info_list = songs_data.stdout.split('\n')
                songs_list_ = []
                if len(songs_info_list) > 4:
                    for _, song in enumerate(songs_info_list):
                        if song.startswith('['):  # '[' 开始的为歌曲信息
                            songs_list_.append(song.replace('&nbsp;', ' ').replace('/nbsp;', ' ')
                                                   .replace('/', '&').replace('&apos;', "' "))
                    for song in songs_list_[:9]:
                        single_song_info = song.strip().split(' ')
                        if len(single_song_info) != 1:  # 去掉空行
                            self.song_id_dict[single_song_info[0][1:3]] = single_song_info[-1]  # 序号和 id 对应
                        single_song_info_ = song.strip().split('-')
                        if len(single_song_info_) != 1:  # 去掉空行
                            self.song_name_dict[single_song_info_[0][1:3]] = single_song_info_[0][5:]  # 序号和 name 对应
                    # 查找到的内容插入文本，并显示
                    display_songs = []
                    for song in songs_list_:
                        display_songs.append('  -  '.join(song.split('-')[:-1]))
                    self.show_song_list.insert('insert', '\n'+'\n\n'.join(display_songs[:9]))
                else:
                    self.song_id_dict = {}
                    self.show_song_list.insert('insert', f'\n Not found songs about {song_title}...')
        self.show_song_list['state'] = 'disabled'


    def download(self):
        """ 下载歌曲 """
        song_number = self.get_song_id()
        song_id = self.song_id_dict.get(song_number, False)
        if song_id:
            if self.is_download_lyric.get():
                subprocess.check_output(f'mxget song --id {song_id} --lyric --force')  # 同时下载歌词，格式 lrc
            else:
                subprocess.check_output(f'mxget song --id {song_id}')  # 只下载歌曲，格式 mp3
            self.show_down_msg['state'] = 'normal'
            self.show_down_msg.insert('1.0', '['+ song_number +'] ' + self.song_name_dict[song_number] + ' - ' +
                                      'Downloaded...\n\n')
            self.show_down_msg['state'] = 'disabled'
        else:
            messagebox.showinfo('Warning', 'Please get valid song info...')

    def get_song_id(self):
        """ 获取要下载对应的歌曲 id """
        song_numbers = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
        return song_numbers[self.song_id_list.current()]


if __name__ == '__main__':
    Application()
