# -*- coding: 1251 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from config import TOKEN_API
from tkinter import messagebox
import requests
import sys


class Ui_MainWindow(object):
    pogoda = {}
    wd = ""
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 298)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(103, 70, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 160, 141, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Разработчик: Veby, TG: @vebytop."))
        self.pushButton.setText(_translate("MainWindow", "Показать погоду!"))
        self.correct_button()
    
    def correct_button(self):
        self.pushButton.clicked.connect(lambda: self.main(self.pushButton.text()))
    
    
    def get_pogoda(self, city, token=TOKEN_API):
        req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric")

        data = req.json()

        code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }


        pod = data["weather"][0]["main"]
        if pod in code_to_smile:
            self.wd = code_to_smile[pod]
        

        self.pogoda = {"Город":data["name"],
                "Температура":data["main"]["temp"],
                "Влажность": data["main"]["humidity"],
                "Давление": data["main"]["pressure"],
                "Скорость ветра": data["wind"]["speed"],
                # "Погода": self.wd
                }
    
    
    def main(self, sity):
        self.get_pogoda(city=sity)

        get_info_pogoda = f"""
        Город: {self.pogoda["Город"]}
        Температура: {round(self.pogoda["Температура"])}
        Влажность: {self.pogoda["Влажность"]}
        Давление: {self.pogoda["Давление"]}
        Скорость ветра: {self.pogoda["Скорость ветра"]}
        Погода: {self.wd}
    """

        messagebox.showinfo("Погода", get_info_pogoda)
        
    
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
