# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiSonDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbPurchasePoint = QtWidgets.QLabel(self.centralwidget)
        self.lbPurchasePoint.setGeometry(QtCore.QRect(610, 230, 109, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.lbPurchasePoint.setFont(font)
        self.lbPurchasePoint.setObjectName("lbPurchasePoint")
        self.lbSalesPoint = QtWidgets.QLabel(self.centralwidget)
        self.lbSalesPoint.setGeometry(QtCore.QRect(760, 230, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.lbSalesPoint.setFont(font)
        self.lbSalesPoint.setObjectName("lbSalesPoint")
        self.lbCoinChart = QtWidgets.QLabel(self.centralwidget)
        self.lbCoinChart.setGeometry(QtCore.QRect(320, 50, 175, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbCoinChart.setFont(font)
        self.lbCoinChart.setObjectName("lbCoinChart")
        self.lbCandleStickChart = QtWidgets.QLabel(self.centralwidget)
        self.lbCandleStickChart.setGeometry(QtCore.QRect(320, 310, 228, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbCandleStickChart.setFont(font)
        self.lbCandleStickChart.setObjectName("lbCandleStickChart")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 266, 401))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox.setMouseTracking(False)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox.setAccessibleName("")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbLow = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbLow.setObjectName("rbLow")
        self.horizontalLayout.addWidget(self.rbLow)
        self.rbModerate = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbModerate.setObjectName("rbModerate")
        self.horizontalLayout.addWidget(self.rbModerate)
        self.rbHigh = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbHigh.setObjectName("rbHigh")
        self.horizontalLayout.addWidget(self.rbHigh)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rbEnableCoinChart = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbEnableCoinChart.setObjectName("rbEnableCoinChart")
        self.horizontalLayout_2.addWidget(self.rbEnableCoinChart)
        self.rbDisabledCoinChart = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbDisabledCoinChart.setObjectName("rbDisabledCoinChart")
        self.horizontalLayout_2.addWidget(self.rbDisabledCoinChart)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rbEnableCandlestick = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbEnableCandlestick.setObjectName("rbEnableCandlestick")
        self.horizontalLayout_3.addWidget(self.rbEnableCandlestick)
        self.rbDisabledCandlestick = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbDisabledCandlestick.setObjectName("rbDisabledCandlestick")
        self.horizontalLayout_3.addWidget(self.rbDisabledCandlestick)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rbEnableProfitRate = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbEnableProfitRate.setObjectName("rbEnableProfitRate")
        self.horizontalLayout_4.addWidget(self.rbEnableProfitRate)
        self.rbDisabledProfitRate = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbDisabledProfitRate.setObjectName("rbDisabledProfitRate")
        self.horizontalLayout_4.addWidget(self.rbDisabledProfitRate)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 570, 121, 40))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(760, 270, 97, 261))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_27 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_9.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_9.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_9.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_9.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_9.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_9.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_9.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_9.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_9.addWidget(self.label_25)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(620, 270, 101, 261))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_26 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_8.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_8.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_8.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_8.addWidget(self.label_16)
        self.coinChart = QtWidgets.QLabel(self.centralwidget)
        self.coinChart.setGeometry(QtCore.QRect(320, 70, 271, 221))
        self.coinChart.setObjectName("coinChart")
        self.candleStickChart = QtWidgets.QLabel(self.centralwidget)
        self.candleStickChart.setGeometry(QtCore.QRect(320, 340, 271, 221))
        self.candleStickChart.setObjectName("candleStickChart")
        self.lbProfitRate = QtWidgets.QLabel(self.centralwidget)
        self.lbProfitRate.setGeometry(QtCore.QRect(600, 70, 170, 45))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lbProfitRate.setFont(font)
        self.lbProfitRate.setObjectName("lbProfitRate")
        self.lbWorkTime = QtWidgets.QLabel(self.centralwidget)
        self.lbWorkTime.setGeometry(QtCore.QRect(600, 110, 245, 16))
        self.lbWorkTime.setObjectName("lbWorkTime")
        self.lbProfitRatePlus = QtWidgets.QLabel(self.centralwidget)
        self.lbProfitRatePlus.setGeometry(QtCore.QRect(600, 150, 234, 57))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lbProfitRatePlus.setFont(font)
        self.lbProfitRatePlus.setObjectName("lbProfitRatePlus")
        self.lbCurrentCoinPrice = QtWidgets.QLabel(self.centralwidget)
        self.lbCurrentCoinPrice.setGeometry(QtCore.QRect(600, 20, 294, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbCurrentCoinPrice.setFont(font)
        self.lbCurrentCoinPrice.setObjectName("lbCurrentCoinPrice")
        self.bottomLeftImage = QtWidgets.QLabel(self.centralwidget)
        self.bottomLeftImage.setGeometry(QtCore.QRect(60, 450, 131, 111))
        self.bottomLeftImage.setObjectName("bottomLeftImage")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 570, 291, 41))
        self.pushButton.setObjectName("pushButton")
        self.bottomRightImage = QtWidgets.QLabel(self.centralwidget)
        self.bottomRightImage.setGeometry(QtCore.QRect(830, 540, 81, 71))
        self.bottomRightImage.setObjectName("bottomRightImage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crypto Agent©"))
        self.lbPurchasePoint.setText(_translate("MainWindow", "Purchase Point"))
        self.lbSalesPoint.setText(_translate("MainWindow", "Sales Point"))
        self.lbCoinChart.setText(_translate("MainWindow", "Coin Chart ( coin/usdt )"))
        self.lbCandleStickChart.setText(_translate("MainWindow", "CandleStick Chart ( coin/usdt )"))
        self.label.setText(_translate("MainWindow", "WHICH COIN DO YOU WANT TO TRADE WITH"))
        self.comboBox.setItemText(1, _translate("MainWindow", "BTC"))
        self.comboBox.setItemText(2, _translate("MainWindow", "ETH"))
        self.comboBox.setItemText(3, _translate("MainWindow", "LTC"))
        self.label_2.setText(_translate("MainWindow", "SELECT RISK LEVEL"))
        self.rbLow.setText(_translate("MainWindow", "Low"))
        self.rbModerate.setText(_translate("MainWindow", "Moderate"))
        self.rbHigh.setText(_translate("MainWindow", "High"))
        self.label_3.setText(_translate("MainWindow", "SHOW COIN CHART"))
        self.rbEnableCoinChart.setText(_translate("MainWindow", "Enable"))
        self.rbDisabledCoinChart.setText(_translate("MainWindow", "Disabled"))
        self.label_4.setText(_translate("MainWindow", "SHOW CANDLESTICK CHART"))
        self.rbEnableCandlestick.setText(_translate("MainWindow", "Enable"))
        self.rbDisabledCandlestick.setText(_translate("MainWindow", "Disabled"))
        self.label_5.setText(_translate("MainWindow", "SHOW CURRENT PROFIT RATE"))
        self.rbEnableProfitRate.setText(_translate("MainWindow", "Enable"))
        self.rbDisabledProfitRate.setText(_translate("MainWindow", "Disabled"))
        self.label_6.setText(_translate("MainWindow", "           AGENT"))
        self.label_7.setText(_translate("MainWindow", "FOR YOUR WALLET.."))
        self.label_27.setText(_translate("MainWindow", "GüncelSatış"))
        self.label_17.setText(_translate("MainWindow", "Sales Data 1"))
        self.label_18.setText(_translate("MainWindow", "Sales Data 2"))
        self.label_19.setText(_translate("MainWindow", "Sales Data 3"))
        self.label_20.setText(_translate("MainWindow", "Sales Data 4"))
        self.label_21.setText(_translate("MainWindow", "Sales Data 5"))
        self.label_22.setText(_translate("MainWindow", "Sales Data 6"))
        self.label_23.setText(_translate("MainWindow", "Sales Data 7"))
        self.label_24.setText(_translate("MainWindow", "Sales Datal 8"))
        self.label_25.setText(_translate("MainWindow", "Sales Data 9"))
        self.label_26.setText(_translate("MainWindow", "Güncel Alış"))
        self.label_8.setText(_translate("MainWindow", "Buy Data 1"))
        self.label_9.setText(_translate("MainWindow", "Buy Data 2"))
        self.label_10.setText(_translate("MainWindow", "Buy Data 3"))
        self.label_11.setText(_translate("MainWindow", "Buy Data 4"))
        self.label_12.setText(_translate("MainWindow", "Buy Data 5"))
        self.label_13.setText(_translate("MainWindow", "Buy Data 6"))
        self.label_14.setText(_translate("MainWindow", "Buy Data 7"))
        self.label_15.setText(_translate("MainWindow", "Buy Data 8"))
        self.label_16.setText(_translate("MainWindow", "Buy Data 9"))
        self.coinChart.setText(_translate("MainWindow", ""))
        self.candleStickChart.setText(_translate("MainWindow", ""))
        self.lbProfitRate.setText(_translate("MainWindow", "Profit Rate"))
        self.lbWorkTime.setText(_translate("MainWindow", "according to transaction so far (workTime)"))
        self.lbProfitRatePlus.setText(_translate("MainWindow", "+ kar oranı"))
        self.lbCurrentCoinPrice.setText(_translate("MainWindow", "Current $coin Price : $coinFiyat"))
        self.bottomLeftImage.setText(_translate("MainWindow", "                      image"))
        self.pushButton.setText(_translate("MainWindow", "Launch Agent"))
        self.bottomRightImage.setText(_translate("MainWindow", "            İmage"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
