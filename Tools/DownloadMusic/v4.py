"""
A tool to download music with mxget and PySide6

# Date: 2021/11/07
# Author: zsh
# Version: v2.0.1
# Python 3.8.1
# PySide6: 6.2.1
# mxget: 1.1.2
"""

import os
import re
import sys
import subprocess
from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QFileDialog

FONT_SIZE = 'font: 12px;'
BASE_DIR = os.path.dirname(__file__)


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.init_ui(self)
        self.song_id_dict = {}  # 歌曲编号与对应的 id
        self.song_name_dict = {}  # 歌曲编号与对应的 name
        self.song_name_and_singer_dict = {}  # 歌曲编号与对应的 name 和 singer

    def init_ui(self, window):
        window.setWindowTitle('DownloadMusic')
        window.setFixedSize(660, 640)
        window.setWindowIcon(QtGui.QIcon(BASE_DIR + '/mico.ico'))
        # row 1
        song_title_label = QtWidgets.QLabel(window)  # 标题
        song_title_label.setText('Song Title')
        song_title_label.setGeometry(10, 10, 90, 25)
        song_title_label.setStyleSheet(FONT_SIZE)

        self.song_title_editor = QtWidgets.QLineEdit(window)  # 输入框
        self.song_title_editor.setGeometry(100, 10, 450, 25)
        self.song_title_editor.setStyleSheet(FONT_SIZE)

        query_btn = QtWidgets.QPushButton(window)  # 查询
        query_btn.setText('Query')
        query_btn.setGeometry(560, 10, 70, 25)
        query_btn.setStyleSheet(FONT_SIZE)
        query_btn.clicked.connect(lambda: self.search())
        # row 2
        song_list_label = QtWidgets.QLabel(window)
        song_list_label.setText('Song List')
        song_list_label.setGeometry(10, 150, 90, 25)
        song_list_label.setStyleSheet(FONT_SIZE)

        self.show_song_list = QtWidgets.QTextBrowser(window)  # 显示歌曲列表
        self.show_song_list.setGeometry(100, 45, 450, 300)
        self.show_song_list.setStyleSheet(FONT_SIZE)
        # row 3
        download_label = QtWidgets.QLabel(window)
        download_label.setText('Download Msg')
        download_label.setGeometry(10, 400, 90, 25)
        download_label.setStyleSheet(FONT_SIZE)

        self.show_download_msg = QtWidgets.QTextBrowser(window)  # 下载信息列表
        self.show_download_msg.setGeometry(100, 350, 450, 140)
        self.show_download_msg.setStyleSheet(FONT_SIZE)
        # row 4
        self.song_numbers = tuple(str(i).zfill(2) for i in range(1, 10))
        self.song_id_list = QtWidgets.QComboBox(window)
        self.song_id_list.addItems(self.song_numbers)
        self.song_id_list.setCurrentIndex(0)
        self.song_id_list.setGeometry(100, 500, 50, 25)
        self.song_id_list.setStyleSheet(FONT_SIZE)

        self.is_download_lyric_cbx = QtWidgets.QCheckBox(window)
        self.is_download_lyric_cbx.setText('Download Lyric')
        self.is_download_lyric_cbx.setGeometry(200, 500, 140, 25)
        self.is_download_lyric_cbx.setStyleSheet('background: rgba(216,216,216,.3);'
                                                 'border: 1px solid rgba(112,112,112,0.8);'
                                                 'border-radius: 2px;'
                                                 'padding-left: 5px;'
                                                 'font: 14px')

        self.music_platforms_dict = {'NeteaseCloud': 'nc', 'QQ': 'qq', 'KuWo': 'kw', "MiGu": 'mg'}
        self.music_platforms = ('NeteaseCloud', 'QQ', 'KuWo', 'MiGu')
        self.change_music_platform = QtWidgets.QComboBox(window)
        self.change_music_platform.addItems(self.music_platforms)
        self.change_music_platform.setCurrentIndex(0)
        self.change_music_platform.setGeometry(350, 500, 110, 25)
        self.change_music_platform.setStyleSheet(FONT_SIZE)
        os.system(r'mxget config --from ' + 'nc')
        # row 5
        self.select_path_btn = QtWidgets.QPushButton(window)
        self.select_path_btn.setText('Select Path')
        self.select_path_btn.setGeometry(100, 535, 90, 25)
        self.select_path_btn.setStyleSheet(FONT_SIZE)
        self.select_path_btn.clicked.connect(lambda: self.set_download_path())

        default_save_to = (os.path.expanduser('~') + '\\Downloads')
        self.save_path = QtWidgets.QTextBrowser(window)
        self.save_path.setGeometry(200, 535, 350, 27)
        self.save_path.setStyleSheet(FONT_SIZE)
        self.save_path.setText(default_save_to)
        os.system(r'mxget config --dir ' + default_save_to)
        # row 5
        self.download_btn = QtWidgets.QPushButton(window)
        self.download_btn.setText('Download')
        self.download_btn.setGeometry(100, 570, 90, 25)
        self.download_btn.setStyleSheet(FONT_SIZE)
        self.download_btn.clicked.connect(lambda: self.download())

    def set_download_path(self):
        """ 选择下载路径 """
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        path = dialog.getExistingDirectory(self, 'select path', 'C:\\', QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if path:
            self.save_path.setText(path.replace("/", os.sep))
            os.system(f'mxget config --dir {path}')

    def set_music_platform(self):
        """ 设置下载平台 """
        platform = self.music_platforms[self.change_music_platform.currentIndex()]
        if not platform == 'NeteaseCloud':
            platform_no = self.music_platforms_dict[platform]
            os.system(f'mxget config --from {platform_no}')

    def search(self):
        """ 查询关键词歌曲 """
        self.set_music_platform()
        song_title = self.song_title_editor.text()  # 获取输入的歌曲名
        if not song_title:  # 没有输入歌名就查询，会出现弹窗警告
            info_msg_box = QtWidgets.QMessageBox()
            info_msg_box.information(QtWidgets.QMainWindow(), 'Info', 'Please input song title...')
            return
        try:
            songs_data = subprocess.run(f'mxget search -k "{song_title}"', stdout=subprocess.PIPE, encoding='gbk')
            songs_list = re.findall(r'\[\d{2}.*', songs_data.stdout.replace('&nbsp;', ' ').replace('/nbsp;', ' ').replace('/', '&').replace('&apos;', "' "))[:len(self.song_numbers)]
            if songs_list:
                display_songs = []
                for song in songs_list:
                    single_song_info = song.strip().split('-')
                    self.song_id_dict[single_song_info[0][1:3]] = single_song_info[-1]  # 序号和id对应
                    self.song_name_dict[single_song_info[0][1:3]] = single_song_info[0]  # 序号和name对应
                    self.song_name_and_singer_dict[single_song_info[0][1:3]] = (single_song_info[1]+ '-' +single_song_info[0][4:]).strip() + '.mp3'
                    display_songs.append('  -  '.join(single_song_info[:-1]))
                self.show_song_list.setText('\n' + '\n\n'.join(display_songs[:len(self.song_numbers)]))
            else:
                self.song_id_dict = {}
                self.show_song_list.setText(f'\n Not found songs about {song_title}...')
        except Exception as e:
            self.show_song_list.setText(f'\n Not found songs about {song_title}....')
            raise e

    def download(self):
        """ 下载歌曲 """
        self.set_music_platform()
        song_number = self.song_numbers[self.song_id_list.currentIndex()]
        song_id = self.song_id_dict.get(song_number, False)
        if song_id:
            download_lyric = ''
            if self.is_download_lyric_cbx.isChecked():
                download_lyric = '--lyric --force'
            subprocess.run(f'mxget song --id {song_id} {download_lyric}')  # 同时下载歌词，格式 lrc
            config_data = subprocess.run('mxget config --show', stdout=subprocess.PIPE, encoding='utf8')
            download_dir = re.search(r'->.*?\n', config_data.stdout).group().replace('->', '').replace('music', '').strip()
            if os.path.exists(os.path.join(download_dir, self.song_name_and_singer_dict[song_number])):
                self.show_download_msg.insertPlainText('\n' + self.song_name_dict[song_number] + ' - ' + 'Downloaded...\n')
            else:
                self.show_download_msg.insertPlainText('\n' + self.song_name_dict[song_number] + ' - ' + 'Unavailable...\n')
            self.show_download_msg.moveCursor(QtGui.QTextCursor.Start)
        else:
            info_msg_box = QtWidgets.QMessageBox()
            info_msg_box.information(QtWidgets.QMainWindow(), 'Info', 'Please get valid song info...')


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())
