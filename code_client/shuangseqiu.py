from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPainter, QPixmap
from port_client import get
from clean import vis
from pre import get_config


config = get_config()
inf = 'LotteryTicket_information'
data = get(config, inf)
dd10, dd30, dd100, dd300 = vis(data)
slot = 0
slot5 = 0
b = 1


class shuangseqiu(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.setLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.setLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.setLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(300)
        self.tableWidget.setHorizontalHeaderLabels(['时间', '期数', '红球', '蓝球'])
        font = QtGui.QFont('微软雅黑', 12)
        font.setBold(True)
        self.tableWidget.horizontalHeader().setFont(font)
        self.tableWidget.horizontalHeader().setStyleSheet('QHeaderView::section{background:gray}')
        self.tableWidget.horizontalHeader().resizeSection(0, 100)
        self.tableWidget.horizontalHeader().resizeSection(1, 100)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().resizeSection(3, 100)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionsClickable(False)

        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.setLayout(self.verticalLayout_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.pix = QPixmap('.\Resources\IMG\cqnu.png')
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)  # 创建像素图元
        self.scene = QtWidgets.QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)  # 将场景添加至视图
        self.verticalLayout_2.addWidget(self.graphicsView)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.tableWidget_1 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_1.setObjectName("tableWidget_1")
        self.tableWidget_1.setColumnCount(7)
        self.tableWidget_1.setRowCount(5)
        self.tableWidget_1.setHorizontalHeaderLabels(['红1', '红2', '红3', '红4', '红5', '红6', '蓝1'])
        self.tableWidget_1.setVerticalHeaderLabels(['众数', 'q1', 'q2', 'q3', '标准差'])
        font = QtGui.QFont('微软雅黑', 12)
        font.setBold(True)
        self.tableWidget_1.horizontalHeader().setFont(font)
        self.tableWidget_1.horizontalHeader().setStyleSheet('QHeaderView::section{background:gray}')
        self.tableWidget_1.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_1.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_1.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_1.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_1.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_1.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_1.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_1.verticalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_1.verticalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_1.verticalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_1.verticalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_1.verticalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_1.horizontalHeader().setSectionsClickable(False)
        self.verticalLayout_2.addWidget(self.tableWidget_1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_3.addWidget(self.pushButton_7)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)

        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.slot1)
        self.pushButton_2.clicked.connect(self.slot2)
        self.pushButton_3.clicked.connect(self.slot3)
        self.pushButton_4.clicked.connect(self.slot4)
        self.pushButton_5.clicked.connect(self.slot5)
        self.pushButton_6.clicked.connect(self.slot6)
        self.pushButton_7.clicked.connect(self.slot7)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "近10期"))
        self.pushButton_2.setText(_translate("MainWindow", "近30期"))
        self.pushButton_3.setText(_translate("MainWindow", "近100期"))
        self.pushButton_4.setText(_translate("MainWindow", "近300期"))
        self.pushButton_5.setText(_translate("MainWindow", "数据可视化"))
        self.pushButton_6.setText(_translate("MainWindow", "统计分析"))
        self.pushButton_7.setText(_translate("MainWindow", "返回主界面"))
        self.label.setText(_translate("MainWindow", "<font color=white>欢迎您进入彩票数据可视化平台！"))

    def slot1(self):
        global slot
        global slot5
        global b
        b = 1
        slot5 = 1
        self.pix = QPixmap('.\Resources\IMG\cqnu.png')
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)  # 创建像素图元
        self.scene = QtWidgets.QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)  # 将场景添加至视图
        self.tableWidget_1.clearContents()
        self.tableWidget.clearContents()
        if slot != 10:
            slot = 10
            self.label.setText( '<font color=white>近 %s 期' % slot)
            for i in range(10):
                for j in range(4):
                    item = QtWidgets.QTableWidgetItem(data[i][j])
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(i, j, item)
        else:
            self.label.setText('<font color=white>欢迎您进入彩票数据可视化平台！')
            slot = 0

    def slot2(self):
        global slot
        global slot5
        global b
        b = 1
        slot5 = 1
        self.pix = QPixmap('.\Resources\IMG\cqnu.png')
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)  # 创建像素图元
        self.scene = QtWidgets.QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)  # 将场景添加至视图
        self.tableWidget_1.clearContents()
        self.tableWidget.clearContents()
        if slot != 30:
            slot = 30
            self.label.setText('<font color=white>近 %s 期' % slot)
            for i in range(30):
                for j in range(4):
                    item = QtWidgets.QTableWidgetItem(data[i][j])
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(i, j, item)
        else:
            self.label.setText('<font color=white>欢迎您进入彩票数据可视化平台！')
            slot = 0

    def slot3(self):
        global slot
        global slot5
        global b
        b = 1
        slot5 = 1
        self.pix = QPixmap('.\Resources\IMG\cqnu.png')
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)  # 创建像素图元
        self.scene = QtWidgets.QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)  # 将场景添加至视图
        self.tableWidget_1.clearContents()
        self.tableWidget.clearContents()
        if slot != 100:
            slot = 100
            self.label.setText('<font color=white>近 %s 期' % slot)
            for i in range(100):
                for j in range(4):
                    item = QtWidgets.QTableWidgetItem(data[i][j])
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(i, j, item)
        else:
            self.label.setText('<font color=white>欢迎您进入彩票数据可视化平台！')
            slot = 0

    def slot4(self):
        global slot
        global slot5
        global b
        b = 1
        slot5 = 1
        self.pix = QPixmap('.\Resources\IMG\cqnu.png')
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)  # 创建像素图元
        self.scene = QtWidgets.QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)  # 将场景添加至视图
        self.tableWidget_1.clearContents()
        self.tableWidget.clearContents()
        if slot != 300:
            slot = 300
            self.label.setText('<font color=white>近 %s 期' % slot)
            for i in range(300):
                for j in range(4):
                    item = QtWidgets.QTableWidgetItem(data[i][j])
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(i, j, item)
        else:
            self.label.setText('<font color=white>欢迎您进入彩票数据可视化平台！')
            slot = 0


    def slot5(self):
        global slot
        global slot5
        if slot != 0:
            self.pix = QPixmap(r'.\Resources\data\%s_%s.svg' % (slot, slot5)if slot5 != 0 else r'.\Resources\IMG\cqnu.png')
            self.item = QtWidgets.QGraphicsPixmapItem(self.pix)  # 创建像素图元
            self.scene = QtWidgets.QGraphicsScene()  # 创建场景
            self.scene.addItem(self.item)
            self.graphicsView.setScene(self.scene)  # 将场景添加至视图
            slot5 = slot5 + 1 if slot5 < 7 else 0

    def slot6(self):
        global slot
        global b
        global dd10
        global dd30
        global dd100
        global dd300
        if b == 1:
            if slot != 0:
                for i in range(5):
                    for j in range(7):
                        if slot == 10: dd = dd10
                        if slot == 30: dd = dd30
                        if slot == 100: dd = dd100
                        if slot == 300: dd = dd300
                        item = QtWidgets.QTableWidgetItem(str(dd[i][j]))
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.tableWidget_1.setItem(i, j, item)
                b = 0
        else:
            self.tableWidget_1.clearContents()
            b = 1

    def slot7(self):
        global slot
        global slot5
        slot = 0
        slot5 = 0
        self.tableWidget.clearContents()
        self.tableWidget_1.clearContents()
        self.label.setText('<font color=white>欢迎您进入彩票数据可视化平台！')
        self.pix = QPixmap('.\Resources\IMG\cqnu.png')
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)  # 创建像素图元
        self.scene = QtWidgets.QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)  # 将场景添加至视图

    def paintEvent(self, event):
        '''
        避免多重传值后的功能失效，从而可以继续使用qss设置样式
        '''
        opt = QtWidgets.QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QtWidgets.QStyle.PE_Widget, opt, painter, self)
