from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QStyleOption, QStyle
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter


class leftNavigation(QWidget):
    '''
    左侧导航栏
    '''

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.left_layout = QGridLayout()  # 创建网格布局对象
        self.setLayout(self.left_layout)  # 将左侧部件设置为网格布局

        # 初始化创建左侧标签和按钮
        self.init_left_close_mini_visit()
        self.init_left_label()
        self.init_left_LotteryTicket_Sort()

        # 将初始化完成的左侧标签、按钮添加进左侧网格布局
        # 最小化、放大还原、关闭部分按钮
        self.left_layout.addWidget(self.left_close, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_mini, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 2, 1, 1)
        # 彩票类型部分的标签和按钮
        self.left_layout.addWidget(self.left_label1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button3, 4, 0, 1, 3)
        # 文件操作分的标签和按钮
        self.left_layout.addWidget(self.left_label2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button5, 7, 0, 1, 3)
        # 联系与帮助
        self.left_layout.addWidget(self.left_label3, 8, 0, 1, 3)

    def init_left_close_mini_visit(self):
        '''
        创建关闭、最小化、放大还原按钮
        '''
        self.left_close = QPushButton("")  # 关闭按钮
        self.left_close.setObjectName('left_close')
        self.left_mini = QPushButton("")  # 最小化按钮
        self.left_mini.setObjectName('left_mini')
        self.left_visit = QPushButton("")  # 空白按钮
        self.left_visit.setObjectName('left_visit')

    def init_left_label(self):
        '''
        左侧标题栏
        '''
        self.left_label1 = QPushButton('彩票类型')
        self.left_label1.setObjectName('left_label')
        self.left_label2 = QPushButton('文件操作')
        self.left_label2.setObjectName('left_label')
        self.left_label3 = QPushButton('联系与帮助')
        self.left_label3.setObjectName('left_label')

    def init_left_LotteryTicket_Sort(self):
        '''
        左侧彩票类型按钮
        '''
        self.left_button1 = QPushButton('双色球')
        self.left_button1.setObjectName('left_button')
        self.left_button1.setIcon(QtGui.QIcon('.\Resources\IMG\shuangseqiu.svg'))

        self.left_button2 = QPushButton('大乐透')
        self.left_button2.setObjectName('left_button')
        self.left_button2.setIcon(QtGui.QIcon('.\Resources\IMG\daletou.png'))

        self.left_button3 = QPushButton('欢乐8')
        self.left_button3.setObjectName('left_button')
        self.left_button3.setIcon(QtGui.QIcon('.\Resources\IMG\huanleba.png'))

        self.left_button4 = QPushButton('另存为')
        self.left_button4.setObjectName('left_button')
        self.left_button4.setIcon(QtGui.QIcon('.\Resources\IMG\lingcunwei.png'))

        self.left_button5 = QPushButton('打印')
        self.left_button5.setObjectName('left_button')
        self.left_button5.setIcon(QtGui.QIcon('.\Resources\IMG\dayin.png'))

    def paintEvent(self, event):
        '''
        避免多重传值后的功能失效，从而可以继续使用qss设置样式
        '''
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
