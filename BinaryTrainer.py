import sys
import time
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication, QObject, QRunnable


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200,200,660,439)
        self.setWindowTitle("Binary Trainer")
        self.initUI()
        self.score = 0
        self.streak = 0
        
    
    def initUI(self):
        self.top_label = QtWidgets.QLabel(self)
        self.top_label.setGeometry(QtCore.QRect(20, 10, 621, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.top_label.setFont(font)
        self.top_label.setObjectName("top_label")
        self.top_label.setText("Binary & Decimal Convertion Trainer")

        self.convertion_table_lable = QtWidgets.QLabel(self)
        self.convertion_table_lable.setGeometry(QtCore.QRect(230, 100, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.convertion_table_lable.setFont(font)
        self.convertion_table_lable.setObjectName("convertion_table_lable")
        self.convertion_table_lable.setText("Convertion Table:")

        self.convertion_table = QtWidgets.QLabel(self)
        self.convertion_table.setGeometry(QtCore.QRect(50, 130, 561, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.convertion_table.setFont(font)
        self.convertion_table.setObjectName("convertion_table")
        self.convertion_table.setText("128  64   32   16   8   4   2   1")

        self.streak_label = QtWidgets.QLabel(self)
        self.streak_label.setGeometry(QtCore.QRect(20, 60, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.streak_label.setFont(font)
        self.streak_label.setObjectName("streak_label")
        self.streak_label.setText("Score:")

        self.streak_result = QtWidgets.QLabel(self)
        self.streak_result.setGeometry(QtCore.QRect(120, 60, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.streak_result.setFont(font)
        self.streak_result.setObjectName("streak_result")
        self.streak_result.setText("0")

        self.streak_label = QtWidgets.QLabel(self)
        self.streak_label.setGeometry(QtCore.QRect(20, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.streak_label.setFont(font)
        self.streak_label.setObjectName("streak_label")
        self.streak_label.setText("Streak:")
        
        self.streak_result = QtWidgets.QLabel(self)
        self.streak_result.setGeometry(QtCore.QRect(120, 90, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.streak_result.setFont(font)
        self.streak_result.setObjectName("streak_result")
        self.streak_result.setText("0")
        
        self.binary_string = QtWidgets.QLabel(self)
        self.binary_string.setGeometry(QtCore.QRect(30, 210, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.binary_string.setFont(font)
        self.binary_string.setObjectName("binary_string")
        
        self.input_octet_1 = QtWidgets.QLineEdit(self)
        self.input_octet_1.setGeometry(QtCore.QRect(50, 250, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.input_octet_1.setFont(font)
        self.input_octet_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_octet_1.setText("")
        self.input_octet_1.setAlignment(QtCore.Qt.AlignCenter)
        self.input_octet_1.setMaxLength(3)
        self.input_octet_1.setObjectName("input_octet_1")
        
        self.input_octet_2 = QtWidgets.QLineEdit(self)
        self.input_octet_2.setGeometry(QtCore.QRect(200, 250, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.input_octet_2.setFont(font)
        self.input_octet_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_octet_2.setText("")
        self.input_octet_2.setAlignment(QtCore.Qt.AlignCenter)
        self.input_octet_2.setMaxLength(3)
        self.input_octet_2.setObjectName("input_octet_2")
        
        self.input_octet_3 = QtWidgets.QLineEdit(self)
        self.input_octet_3.setGeometry(QtCore.QRect(350, 250, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.input_octet_3.setFont(font)
        self.input_octet_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_octet_3.setText("")
        self.input_octet_3.setAlignment(QtCore.Qt.AlignCenter)
        self.input_octet_3.setMaxLength(3)
        self.input_octet_3.setObjectName("input_octet_3")
        
        self.input_octet_4 = QtWidgets.QLineEdit(self)
        self.input_octet_4.setGeometry(QtCore.QRect(500, 250, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.input_octet_4.setFont(font)
        self.input_octet_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_octet_4.setText("")
        self.input_octet_4.setAlignment(QtCore.Qt.AlignCenter)
        self.input_octet_4.setObjectName("input_octet_4")
        self.input_octet_4.setMaxLength(3)
        self.streak_label.setText("Score:")
    
        self.label_result = QtWidgets.QLabel(self)
        self.label_result.setGeometry(QtCore.QRect(290, 290, 105, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.label_result.setText("")
        
        self.button_check = QtWidgets.QPushButton(self)
        self.button_check.setGeometry(QtCore.QRect(260, 340, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.button_check.setFont(font)
        self.button_check.setObjectName("button_check")
        self.button_check.setText("Check")
        self.button_check.clicked.connect(self.verify)

    def q_decimal(self):
        octet_1 = random.randint(0, 255)
        octet_2 = random.randint(0, 255)
        octet_3 = random.randint(0, 255)
        octet_4 = random.randint(0, 255)
        return f"{octet_1}.{octet_2}.{octet_3}.{octet_4}"
        
    def q_binary(self, decimal_string):
        binary_string = ""
        for num in decimal_string.split("."):
            binary_string += str("{0:08b}.".format(int(num)))
        return binary_string[:-1]
    
    def question(self):
        num_string = self.q_decimal()
        bin_string = self.q_binary(num_string)
        self.binary_string.setText(bin_string)
        return num_string

    def verify(self):
        octet_1 = self.input_octet_1.text()
        octet_2 = self.input_octet_2.text()
        octet_3 = self.input_octet_3.text()
        octet_4 = self.input_octet_4.text()
        result_string = f"{octet_1}.{octet_2}.{octet_3}.{octet_4}"
        right_answer = self.question()
        if right_answer == result_string:
            self.score += 1
            self.streak += 1
            self.label_result.setText("Correct")
            time.sleep(1)
            self.label_result.setText("")
            print("Correct!")
        else:
            if self.streak > 0:
                self.streak -= 1
            self.label_result.setText("Incorrect")
            time.sleep(1)
            self.label_result.setText("")
            print("Incorrect!")
        self.question()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
