from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QCursor, QPixmap
from PyQt5.QtCore import Qt
from leftNavigation import leftNavigation
from shuangseqiu import shuangseqiu
from daletou import daletou
from huanleba import huanleba
from lingcunwei import lingcunwei
from dayin import dayin


class LotteryTicketSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        '''
        初始化整体布局
        '''
        self.resize(1200, 800)
        self.desktopWidth = QApplication.desktop().width()  # 获取当前桌面的宽
        self.desktopHeight = QApplication.desktop().height()  # 获取当前桌面的高

        self.main_widget = QWidget()  # 创建窗口主部件
        self.main_widget.setObjectName('main_widget')  # 对象命名
        self.main_layout = QGridLayout()  # 创建网格布局的对象
        self.main_widget.setLayout(self.main_layout)  # 将主部件设置为网格布局

        self.init_left()  # 初始化左侧空间
        self.init_right()  # 初始化右侧空间

        # 添加左侧导航栏，右侧主界面、双色球界面、大乐透界面、欢乐8界面、另存为界面、打印界面
        self.main_layout.addWidget(self.left_widget, 0, 0, 1, 1)
        self.main_layout.addWidget(self.right_widget, 0, 1, 1, 6)

        self.main_layout.addWidget(self.shuangseqiu_widget, 0, 1, 1, 6)
        self.main_layout.addWidget(self.daletou_widget, 0, 1, 1, 6)
        self.main_layout.addWidget(self.huanleba_widget, 0, 1, 1, 6)
        self.main_layout.addWidget(self.lingcunwei_widget, 0, 1, 1, 6)
        self.main_layout.addWidget(self.dayin_widget, 0, 1, 1, 6)

        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        # 窗口属性设置
        self.setWindowOpacity(0.975)  # 设置窗口透明度
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框
        self.main_layout.setSpacing(0)  # 取出左右之间的缝隙

    def init_left(self):
        '''
        初始化左侧布局
        '''
        self.left_widget = leftNavigation()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')  # 左侧部件对象命名

        self.left_widget.left_close.clicked.connect(self.closeWindow)

        self.left_widget.left_visit.clicked.connect(self.visitWindow)
        self.left_widget.left_mini.clicked.connect(self.minimizeWindow)
        self.visitFlag = False

        self.left_widget.left_button1.clicked.connect(self.into_shuangseqiuView)
        self.left_widget.left_button2.clicked.connect(self.into_daletouView)
        self.left_widget.left_button3.clicked.connect(self.into_huanlebaView)
        self.left_widget.left_button4.clicked.connect(self.into_lingcunweiView)
        self.left_widget.left_button5.clicked.connect(self.into_dayinView)

    def init_right(self):
        '''
        初始化右侧布局
        '''
        self.main_view()

        self.shuangseqiu_view()

        self.daletou_view()
        self.huanleba_view()
        self.lingcunwei_view()
        self.dayin_view()

    def main_view(self):
        '''
        用于介绍的主界面
        '''
        self.right_widget = QWidget()  # 创建右侧界面1
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QGridLayout()  # 创建网格布局对象1
        self.right_widget.setLayout(self.right_layout)  # 设置右侧界面1的布局为网格布局
        # 支撑空间
        self.label1 = QLabel()
        self.right_layout.addWidget(self.label1, 0, 0, 2, 4)

        self.lb1 = QLabel()
        self.pix = QPixmap('.\Resources\IMG\cqnu.png')
        self.lb1.setGeometry(0, 0, self.pix.width(), self.pix.height())
        self.lb1.setPixmap(self.pix)

        self.cqnu_text=QLabel()
        cqnu = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Kaiti'; font-size:9pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:24pt; font-weight:600;">重庆师范大学数学科学学院</span></p></body></html>'''
        self.cqnu_text.setText(cqnu)
        self.cqnu_text.setObjectName('cqnu')

        self.cqnu_layout = QHBoxLayout()
        self.cqnu_layout.addWidget(self.lb1)
        self.cqnu_layout.addWidget(self.cqnu_text)
        self.right_layout.addLayout(self.cqnu_layout, 0, 0, 1, 3)

        self.label_introduction = QLabel()
        introduction = '''<div style="text-align:center; font-size: 50px;font-family:'Microsoft Yahei'; color:white;"><b>彩票数据可视化平台</b></div> '''
        self.label_introduction.setText(introduction)
        self.label_introduction.setObjectName('introduction')
        self.right_layout.addWidget(self.label_introduction, 3, 1, 3, 3)

        self.label_member = QLabel()
        member = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'SimHei'; font-size:12pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Microsoft Yahei'; font-weight:600; font-size:14pt;">制作人员</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;"><br /></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">王云龙 文驰骋 朱泓旭</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;"><br /></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">陈昊 宣凯恒 黄珍妮</p></body></html>'''
        self.label_member.setText(member)
        self.label_member.setObjectName('member')
        self.right_layout.addWidget(self.label_member, 7, 4, 2, 1)

        self.noneLabel1_2 = QLabel()  # 用来支撑空间
        self.right_layout.addWidget(self.noneLabel1_2, 5, 0, 2, 4)

    def shuangseqiu_view(self):
        self.shuangseqiu_widget = shuangseqiu()
        self.shuangseqiu_widget.setObjectName('shuangseqiu_widget')
        self.shuangseqiu_widget.pushButton_7.clicked.connect(self.return_mainView)
        self.shuangseqiu_widget.hide()

    def daletou_view(self):
        self.daletou_widget = daletou()
        self.daletou_widget.setObjectName('daletou_widget')
        self.daletou_widget.pushButton_10.clicked.connect(self.return_mainView)
        self.daletou_widget.hide()

    def huanleba_view(self):
        self.huanleba_widget = huanleba()
        self.huanleba_widget.setObjectName('huanleba_widget')
        self.huanleba_widget.pushButton_10.clicked.connect(self.return_mainView)
        self.huanleba_widget.hide()

    def lingcunwei_view(self):
        self.lingcunwei_widget = lingcunwei()
        self.lingcunwei_widget.setObjectName('lingcunwei_widget')
        self.lingcunwei_widget.pushButton_10.clicked.connect(self.return_mainView)
        self.lingcunwei_widget.hide()

    def dayin_view(self):
        self.dayin_widget = dayin()
        self.dayin_widget.setObjectName('dayin_widget')
        self.dayin_widget.pushButton_10.clicked.connect(self.return_mainView)
        self.dayin_widget.hide()

    def return_mainView(self):
        self.right_widget.show()
        self.shuangseqiu_widget.hide()
        self.daletou_widget.hide()
        self.huanleba_widget.hide()
        self.lingcunwei_widget.hide()
        self.dayin_widget.hide()

    def into_shuangseqiuView(self):
        self.shuangseqiu_widget.show()
        self.daletou_widget.hide()
        self.huanleba_widget.hide()
        self.lingcunwei_widget.hide()
        self.dayin_widget.hide()
        self.right_widget.hide()

    def into_daletouView(self):
        self.daletou_widget.show()
        self.huanleba_widget.hide()
        self.lingcunwei_widget.hide()
        self.dayin_widget.hide()
        self.shuangseqiu_widget.hide()
        self.right_widget.hide()

    def into_huanlebaView(self):
        self.huanleba_widget.show()
        self.daletou_widget.hide()
        self.lingcunwei_widget.hide()
        self.dayin_widget.hide()
        self.shuangseqiu_widget.hide()
        self.right_widget.hide()

    def into_lingcunweiView(self):
        self.lingcunwei_widget.show()
        self.daletou_widget.hide()
        self.huanleba_widget.hide()
        self.dayin_widget.hide()
        self.shuangseqiu_widget.hide()
        self.right_widget.hide()

    def into_dayinView(self):
        self.dayin_widget.show()
        self.daletou_widget.hide()
        self.huanleba_widget.hide()
        self.lingcunwei_widget.hide()
        self.shuangseqiu_widget.hide()
        self.right_widget.hide()

    def closeWindow(self):
        '''
        close按钮对应的关闭窗口
        '''
        self.close()

    def minimizeWindow(self):
        '''
        mini按钮对应的最小化窗口
        '''
        self.showMinimized()

    def visitWindow(self):
        '''
        visit按钮对应的全屏or还原窗口大小
        '''
        if self.visitFlag == False:
            self.lastWidth = self.width()
            self.lastHeight = self.height()
            self.resize(self.desktopWidth, self.desktopHeight)
            x = (self.desktopWidth - self.width()) // 2
            y = (self.desktopHeight - self.height()) // 2
            self.move(x, y)
            self.visitFlag = True
        else:
            self.resize(self.lastWidth, self.lastHeight)
            x = (self.desktopWidth - self.width()) // 2
            y = (self.desktopHeight - self.height()) // 2
            self.move(x, y)
            # print('origin')
            self.visitFlag = False

    def mousePressEvent(self, QMouseEvent):
        '''
        redefine已有的鼠标按下事件
        '''
        if QMouseEvent.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = QMouseEvent.globalPos()-self.pos()  # 获取鼠标相对窗口的位置
            QMouseEvent.accept()
            # self.setCursor(QCursor(Qt.WaitCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        '''
        redefine已有的鼠标移动事件
        '''
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        '''
        redefine已有的鼠标释放事件
        '''
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
