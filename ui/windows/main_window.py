# coding:utf-8
import sys

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, FluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition)
from qfluentwidgets import FluentIcon as FIF


from ui.page.Setting.setting_page import SettingPage


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)     # label标签
        self.hBoxLayout = QHBoxLayout(self)           # 创建一个水平布局（QHBoxLayout），用于管理子控件的排列方式。

        setFont(self.label, 24)   # 设置字体
        self.label.setAlignment(Qt.AlignCenter)         # 设置标签的文本对齐方式为居中对齐。Qt.AlignCenter 是 Qt 中的一个枚举值，表示居中对齐。
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        #         #将 self.label 添加到水平布局中。
#
# 参数：
#
# self.label：要添加的控件。
#
# 1：控件的拉伸因子（stretch factor），表示标签在布局中占据的比例。
#
# Qt.AlignCenter：控件在布局中的对齐方式为居中对齐。
        self.setObjectName(text.replace(' ', '-'))


class Window(FluentWindow):

    def __init__(self):
        super().__init__()

        # create sub interface
        self.homeInterface = Widget('导航页面', self)
        # self.downloadVideoInterface = DownloadPage(self)
        # self.voiceSeparationInterface = VoiceSeparationPage(self)
        self.transcriptionInterface = Widget('视频转录', self)
        self.translationInterface = Widget('模型翻译', self)
        self.subtitleInterface = Widget('字幕处理', self)
        self.alltaskInterface = Widget('任务列表', self)
        self.settingInterface = SettingPage(self)

        self.initNavigation()
        self.initWindow()

    # 导航栏的初始化
    def initNavigation(self):
        # 通过调用 addSubInterface 方法添加多个导航项
        # addSUbInterface(对象，图标，文本,(父类)）
        self.addSubInterface(self.homeInterface, FIF.HOME, '主页')

        self.navigationInterface.addSeparator()  # 分割线

        # self.addSubInterface(self.downloadVideoInterface, FIF.DOWN, '下载视频', NavigationItemPosition.SCROLL)
        # self.addSubInterface(self.voiceSeparationInterface, FIF.MUSIC, '人声分离', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.transcriptionInterface, FIF.VIDEO, '视频转录', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.translationInterface, FIF.SEND, '模型翻译', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.subtitleInterface, FIF.CUT, '字幕处理', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.alltaskInterface, FIF.TILES, '任务列表', NavigationItemPosition.SCROLL)
        # add custom widget to bottom
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('Cherishzz', 'resource/shoko.png'),
            onClick=self.showMessageBox,
            position=NavigationItemPosition.BOTTOM,
        )

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)




    # 初始化应用程序的主窗口
    def initWindow(self):
        self.resize(900, 700) # 设置窗口大小
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))  #T图标
        self.setWindowTitle('PyQt-Fluent-Widgets')    # 窗口主题

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
        # 将窗口居中显示
        # set the minimum window width that allows the navigation panel to be expanded
        # self.navigationInterface.setMinimumExpandWidth(900)
        # self.navigationInterface.expand(useAni=False)

    def showMessageBox(self):
        w = MessageBox(
            '支持作者🥰',
            '个人开发不易，如果这个项目帮助到了您，可以考虑请作者喝一瓶快乐水🥤。您的支持就是作者开发和维护项目的动力🚀',
            self
        )
        w.yesButton.setText('来啦老弟')
        w.cancelButton.setText('下次一定')

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://www.baidu.com"))