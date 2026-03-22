from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from qfluentwidgets import (
    SubtitleLabel, BodyLabel, CardWidget, ComboBox, ScrollArea, ExpandLayout,
    setFont, setTheme, Theme
)




class SettingPage(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)
        self._setup_ui()
        self.setObjectName("SettingPage")

    def _setup_ui(self):
        # ScrollArea 自身配置
        # setWidget设置滚动的内容
        # 设置scrollWidget 自动跟随 ScrollArea 尺寸变化
        # 关闭横向滚动条
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)



