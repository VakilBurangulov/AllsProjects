from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def __init__(self):
        self.is_equal = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 375, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_result.setStyleSheet("background-color: rgb(169, 166, 170);\n"
"color: rgb(255, 255, 255);")
        self.label_result.setObjectName("label_result")
        self.btn_zero = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zero.setGeometry(QtCore.QRect(0, 320, 150, 80))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.btn_zero.setFont(font)
        self.btn_zero.setStyleSheet("background-color: rgb(255, 199, 107);")
        self.btn_zero.setObjectName("btn_zero")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(150, 320, 150, 80))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(255, 136, 120);")
        self.btn_equal.setObjectName("btn_equal")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 230, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(255, 199, 107);")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 230, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(255, 199, 107);")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(200, 230, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(255, 199, 107);")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 140, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(255, 199, 107);")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 140, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(255, 199, 107);")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(200, 140, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(255, 199, 107);")
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 50, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(255, 199, 107);")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 50, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(255, 199, 107);")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(200, 50, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(255, 199, 107);")
        self.btn_9.setObjectName("btn_9")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(300, 50, 75, 90))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("background-color: rgb(255, 199, 107);")
        self.btn_add.setObjectName("btn_add")
        self.btn_sub = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sub.setGeometry(QtCore.QRect(300, 140, 75, 90))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.btn_sub.setFont(font)
        self.btn_sub.setStyleSheet("background-color: rgb(255, 199, 107);")
        self.btn_sub.setObjectName("btn_sub")
        self.btn_mul = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mul.setGeometry(QtCore.QRect(300, 230, 75, 90))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.btn_mul.setFont(font)
        self.btn_mul.setStyleSheet("background-color: rgb(255, 199, 107);")
        self.btn_mul.setObjectName("btn_mul")
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        self.btn_div.setGeometry(QtCore.QRect(300, 320, 75, 80))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.btn_div.setFont(font)
        self.btn_div.setStyleSheet("background-color: rgb(255, 199, 107);")
        self.btn_div.setObjectName("btn_div")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

        self.is_equal = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.btn_zero.setText(_translate("MainWindow", "0"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_sub.setText(_translate("MainWindow", "-"))
        self.btn_mul.setText(_translate("MainWindow", "*"))
        self.btn_div.setText(_translate("MainWindow", "/"))

    def add_functions(self):
        self.btn_zero.clicked.connect(lambda: self.write_number(self.btn_zero.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_add.clicked.connect(lambda: self.write_number(self.btn_add.text()))
        self.btn_div.clicked.connect(lambda: self.write_number(self.btn_div.text()))
        self.btn_mul.clicked.connect(lambda: self.write_number(self.btn_mul.text()))
        self.btn_sub.clicked.connect(lambda: self.write_number(self.btn_sub.text()))

        self.btn_equal.clicked.connect(self.results)

    def write_number(self, number):
        if self.label_result.text() == "0" or self.is_equal:
            self.label_result.setText(number)
            self.is_equal = False
        else:
            self.label_result.setText(self.label_result.text() + number)

    def results(self):
        if not self.is_equal:
            res = eval(self.label_result.text())
            self.label_result.setText("Результат: " + str(res))
            self.is_equal = True
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Сейчас это действие выполнить нельзя")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Reset | QMessageBox.Ok | QMessageBox.Cancel)

            error.setDefaultButton(QMessageBox.Ok)
            error.setInformativeText("Два раза действие не выполнить")
            error.setDetailedText("Детали")

            error.buttonClicked.connect(self.popup_action)

            error.exec_()

    def popup_action(self, btn: QMessageBox):
        if btn.text() == "Ok":
            print("Print ok")
        elif btn.text() == "Reset":
            self.label_result.setText("")
            self.is_equal = False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
