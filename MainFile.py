import sqlite3
import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from qtpy import QtGui

from Detectiv1 import Ui_MainWindow
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from Character import Character
from FinishGame import game_ower


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Ставлю обложки картам
        self.labels = [self.label, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7,
                       self.label_8, self.label_9, self.label_10, self.num1, self.num2, self.num3, self.num4, self.num5,
                       self.num6, self.num7, self.num8, self.num9, self.num10]
        for label in self.labels[:10]:
            self.pixmap = QPixmap('ДетективМ.png')
            label.resize(70, 110)
            label.setPixmap(self.pixmap)
        for label in self.labels[10:]:
            label.setStyleSheet("background-color: black;color: white")
        self.game_name.setStyleSheet("color: white")
        # Делаю фон
        oImage = QImage("los_angeles_city.jpg")
        sImage = oImage.scaled(QSize(1113, 658))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.play.setStyleSheet("background-color: #d11316;color: white")
        self.play.clicked.connect(self.game)
        # Ставлю флаги
        self.Check = False
        self.Kill = False
        self.flag_night = False
        self.flag_day = False
        self.flag = False
        self.dead_list = []


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_C and self.flag:
            self.Check = True
            self.Kill = False
            self.textEdit.append("\nНажмити клавишу, соответствующую номеру игрока, которого вы хотите проверить" +
                                 "(для игрока под номером 10 соответствующая клавиша 0)")
        if event.key() == Qt.Key_K and self.flag:
            self.Check = False
            self.Kill = True
            self.textEdit.append("\nНажмити клавишу, соответствующую номеру игрока, которого вы хотите казнить" +
                                 "(для игрока под номером 10 соответствующая клавиша 0)")
        if event.key() == Qt.Key_1 and self.Check:
            self.flag = False
            if self.character1.checked() == 0:
                self.textEdit.append("\nИгрок номер 1 является МИРНЫМ")
            if self.character1.checked() == 1:
                self.textEdit.append("\nИгрок номер 1 является БАНДИТОМ")
            self.Check = False
            self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
            self.flag_night = True

        if event.key() == Qt.Key_2 and self.Check:
            self.flag = False
            if self.character2.checked() == 0:
                self.textEdit.append("\nИгрок номер 2 является МИРНЫМ")
            if self.character2.checked() == 1:
                self.textEdit.append("\nИгрок номер 2 является БАНДИТОМ")
            self.Check = False
            self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
            self.flag_night = True

        if event.key() == Qt.Key_3 and self.Check:
            self.flag = False
            if self.character3.checked() == 0:
                self.textEdit.append("\nИгрок номер 3 является МИРНЫМ")
            if self.character3.checked() == 1:
                self.textEdit.append("\nИгрок номер 3 является БАНДИТОМ")
            self.Check = False
            self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
            self.flag_night = True
        if event.key() == Qt.Key_4 and self.Check:
            self.flag = False
            if self.character4.checked() == 0:
                self.textEdit.append("\nИгрок номер 4 является МИРНЫМ")
            if self.character4.checked() == 1:
                self.textEdit.append("\nИгрок номер 4 является БАНДИТОМ")
            self.Check = False
            self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
            self.flag_night = True
        if event.key() == Qt.Key_5 and self.Check:
            self.flag = False
            if self.character5.checked() == 0:
                self.textEdit.append("\nИгрок номер 5 является МИРНЫМ")
            if self.character5.checked() == 1:
                self.textEdit.append("\nИгрок номер 5 является БАНДИТОМ")
            self.Check = False
            self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
            self.flag_night = True
        if event.key() == Qt.Key_6 and self.Check:
            self.flag = False
            if self.character6.checked() == 0:
                self.textEdit.append("\nИгрок номер 6 является МИРНЫМ")
            if self.character6.checked() == 1:
                self.textEdit.append("\nИгрок номер 6 является БАНДИТОМ")
            self.Check = False
            self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
            self.flag_night = True
        if event.key() == Qt.Key_7 and self.Check:
            self.flag = False
            if self.character7.checked() == 0:
                self.textEdit.append("\nИгрок номер 7 является МИРНЫМ")
            if self.character7.checked() == 1:
                self.textEdit.append("\nИгрок номер 7 является БАНДИТОМ")
            self.Check = False
            self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
            self.flag_night = True
        if event.key() == Qt.Key_8 and self.Check:
            self.flag = False
            if self.character8.checked() == 0:
                self.textEdit.append("\nИгрок номер 8 является МИРНЫМ")
            if self.character8.checked() == 1:
                self.textEdit.append("\nИгрок номер 8 является БАНДИТОМ")
            self.Check = False
            self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
            self.flag_night = True
        if event.key() == Qt.Key_9 and self.Check:
            self.flag = False
            if self.character9.checked() == 0:
                self.textEdit.append("\nИгрок номер 9 является МИРНЫМ")
            if self.character9.checked() == 1:
                self.textEdit.append("\nИгрок номер 9 является БАНДИТОМ")
            self.Check = False
            self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
            self.flag_night = True
        if event.key() == Qt.Key_0 and self.Check:
            self.flag = False
            if self.character10.checked() == 0:
                self.textEdit.append("\nИгрок номер 10 является МИРНЫМ")
            if self.character10.checked() == 1:
                self.textEdit.append("\nИгрок номер 10 является БАНДИТОМ")
            self.Check = False
            self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
            self.flag_night = True
        if event.key() == Qt.Key_1 and self.Kill:
            self.flag = False
            role = self.character1.dead()
            if role == 1:
                self.pixmap = QPixmap("бандитМ.png")
                self.label.resize(70, 110)
                self.label.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 1 и он является Бандитом")
            if role == 0:
                self.pixmap = QPixmap("мирныйМ.png")
                self.label.resize(70, 110)
                self.label.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 1 и он является МИРНЫМ")
            self.Kill = False
            self.dead_list.append(1)
            if game_ower(self.dead_list, "DetectivBD.db").check() == 1:
                self.game_ower.setText("Вы Проиграли")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            elif game_ower(self.dead_list, "DetectivBD.db").check() == 2:
                self.game_ower.setText("Вы Победили")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            else:
                self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
                self.flag_night = True
        if event.key() == Qt.Key_2 and self.Kill:
            self.flag = False
            role = self.character2.dead()
            if role == 1:
                self.pixmap = QPixmap("бандитМ.png")
                self.label_2.resize(70, 110)
                self.label_2.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 2 и он является Бандитом")
            if role == 0:
                self.pixmap = QPixmap("мирныйМ.png")
                self.label_2.resize(70, 110)
                self.label_2.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 2 и он является МИРНЫМ")
            self.Kill = False
            self.dead_list.append(2)
            if game_ower(self.dead_list, "DetectivBD.db").check() == 1:
                self.game_ower.setText("Вы Проиграли")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            elif game_ower(self.dead_list, "DetectivBD.db").check() == 2:
                self.game_ower.setText("Вы Победили")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            else:
                self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
                self.flag_night = True
        if event.key() == Qt.Key_3 and self.Kill:
            self.flag = False
            role = self.character3.dead()
            if role == 1:
                self.pixmap = QPixmap("бандитМ.png")
                self.label_3.resize(70, 110)
                self.label_3.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 3 и он является Бандитом")
            if role == 0:
                self.pixmap = QPixmap("мирныйМ.png")
                self.label_3.resize(70, 110)
                self.label_3.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 3 и он является МИРНЫМ")
            self.Kill = False
            self.dead_list.append(3)
            if game_ower(self.dead_list, "DetectivBD.db").check() == 1:
                self.game_ower.setText("Вы Проиграли")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            elif game_ower(self.dead_list, "DetectivBD.db").check() == 2:
                self.game_ower.setText("Вы Победили")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            else:
                self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
                self.flag_night = True
        if event.key() == Qt.Key_4 and self.Kill:
            self.flag = False
            role = self.character4.dead()
            if role == 1:
                self.pixmap = QPixmap("бандитМ.png")
                self.label_4.resize(70, 110)
                self.label_4.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 4 и он является Бандитом")
            if role == 0:
                self.pixmap = QPixmap("мирныйМ.png")
                self.label_4.resize(70, 110)
                self.label_4.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 4 и он является МИРНЫМ")
            self.Kill = False
            self.dead_list.append(4)
            if game_ower(self.dead_list, "DetectivBD.db").check() == 1:
                self.game_ower.setText("Вы Проиграли")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            elif game_ower(self.dead_list, "DetectivBD.db").check() == 2:
                self.game_ower.setText("Вы Победили")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            else:
                self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
                self.flag_night = True
        if event.key() == Qt.Key_5 and self.Kill:
            self.flag = False
            role = self.character5.dead()
            if role == 1:
                self.pixmap = QPixmap("бандитМ.png")
                self.label_5.resize(70, 110)
                self.label_5.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 5 и он является Бандитом")
            if role == 0:
                self.pixmap = QPixmap("мирныйМ.png")
                self.label_5.resize(70, 110)
                self.label_5.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 5 и он является МИРНЫМ")
            self.Kill = False
            self.dead_list.append(5)
            if game_ower(self.dead_list, "DetectivBD.db").check() == 1:
                self.game_ower.setText("Вы Проиграли")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            elif game_ower(self.dead_list, "DetectivBD.db").check() == 2:
                self.game_ower.setText("Вы Победили")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            else:
                self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
                self.flag_night = True
        if event.key() == Qt.Key_6 and self.Kill:
            self.flag = False
            role = self.character6.dead()
            if role == 1:
                self.pixmap = QPixmap("бандитМ.png")
                self.label_6.resize(70, 110)
                self.label_6.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 6 и он является Бандитом")
            if role == 0:
                self.pixmap = QPixmap("мирныйМ.png")
                self.label_6.resize(70, 110)
                self.label_6.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 6 и он является МИРНЫМ")
            self.Kill = False
            self.dead_list.append(6)
            if game_ower(self.dead_list, "DetectivBD.db").check() == 1:
                self.game_ower.setText("Вы Проиграли")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            elif game_ower(self.dead_list, "DetectivBD.db").check() == 2:
                self.game_ower.setText("Вы Победили")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            else:
                self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
                self.flag_night = True
        if event.key() == Qt.Key_7 and self.Kill:
            self.flag = False
            role = self.character7.dead()
            if role == 1:
                self.pixmap = QPixmap("бандитМ.png")
                self.label_7.resize(70, 110)
                self.label_7.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 7 и он является Бандитом")
            if role == 0:
                self.pixmap = QPixmap("мирныйМ.png")
                self.label_7.resize(70, 110)
                self.label_7.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 7 и он является МИРНЫМ")
            self.Kill = False
            self.dead_list.append(7)
            if game_ower(self.dead_list, "DetectivBD.db").check() == 1:
                self.game_ower.setText("Вы Проиграли")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            elif game_ower(self.dead_list, "DetectivBD.db").check() == 2:
                self.game_ower.setText("Вы Победили")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            else:
                self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
                self.flag_night = True
        if event.key() == Qt.Key_8 and self.Kill:
            self.flag = False
            role = self.character8.dead()
            if role == 1:
                self.pixmap = QPixmap("бандитМ.png")
                self.label_8.resize(70, 110)
                self.label_8.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 8 и он является Бандитом")
            if role == 0:
                self.pixmap = QPixmap("мирныйМ.png")
                self.label_8.resize(70, 110)
                self.label_8.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 8 и он является МИРНЫМ")
            self.Kill = False
            self.dead_list.append(8)
            if game_ower(self.dead_list, "DetectivBD.db").check() == 1:
                self.game_ower.setText("Вы Проиграли")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            elif game_ower(self.dead_list, "DetectivBD.db").check() == 2:
                self.game_ower.setText("Вы Победили")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            else:
                self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
                self.flag_night = True
        if event.key() == Qt.Key_9 and self.Kill:
            self.flag = False
            role = self.character9.dead()
            if role == 1:
                self.pixmap = QPixmap("бандитМ.png")
                self.label_9.resize(70, 110)
                self.label_9.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 9 и он является Бандитом")
            if role == 0:
                self.pixmap = QPixmap("мирныйМ.png")
                self.label_9.resize(70, 110)
                self.label_9.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 9 и он является МИРНЫМ")
            self.Kill = False
            self.dead_list.append(9)
            if game_ower(self.dead_list, "DetectivBD.db").check() == 1:
                self.game_ower.setText("Вы Проиграли")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            elif game_ower(self.dead_list, "DetectivBD.db").check() == 2:
                self.game_ower.setText("Вы Победили")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            else:
                self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
                self.flag_night = True
        if event.key() == Qt.Key_0 and self.Kill:
            self.flag = False
            role = self.character10.dead()
            if role == 1:
                self.pixmap = QPixmap("бандитМ.png")
                self.label_10.resize(70, 110)
                self.label_10.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 10 и он является Бандитом")
            if role == 0:
                self.pixmap = QPixmap("мирныйМ.png")
                self.label_10.resize(70, 110)
                self.label_10.setPixmap(self.pixmap)
                self.textEdit.append("\nВы казнили игрока номер 10 и он является МИРНЫМ")
            self.Kill = False
            self.dead_list.append(10)
            if game_ower(self.dead_list, "DetectivBD.db").check() == 1:
                self.game_ower.setText("Вы Проиграли")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            elif game_ower(self.dead_list, "DetectivBD.db").check() == 2:
                self.game_ower.setText("Вы Победили")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            else:
                self.textEdit.append("\nНажмите клавишу W, чтобы начать ночь")
                self.flag_night = True
        if event.key() == Qt.Key_W:
            if self.flag_night:
                self.flag_night = False
                victim = self.character1.night(self.dead_list)
                if victim == 1:
                    self.character1.dead()
                elif victim == 2:
                    self.character2.dead()
                elif victim == 3:
                    self.character3.dead()
                elif victim == 4:
                    self.character4.dead()
                elif victim == 5:
                    self.character5.dead()
                elif victim == 6:
                    self.character6.dead()
                elif victim == 7:
                    self.character7.dead()
                elif victim == 8:
                    self.character8.dead()
                elif victim == 9:
                    self.character9.dead()
                elif victim == 10:
                    self.character10.dead()
                self.dead_list.append(victim)
                self.pixmap = QPixmap("мирныйМ.png")
                self.labels[victim - 1].resize(70, 110)
                self.labels[victim - 1].setPixmap(self.pixmap)
                self.textEdit.append("\nБыл убит игрок номер {}".format(str(victim)))
                self.textEdit.append("\nНажмите клавишу S, чтобы начать день")
                self.flag_day = True

        if event.key() == Qt.Key_S:
            if game_ower(self.dead_list, "DetectivBD.db").check() == 1:
                self.game_ower.setText("Вы Проиграли")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)
            elif game_ower(self.dead_list, "DetectivBD.db").check() == 2:
                self.game_ower.setText("Вы Победили")
                self.game_ower.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
                self.game_ower.setStyleSheet("background-color: black;color: white")
                for num, label in enumerate(self.labels[:10]):
                    result = game_ower(self.dead_list, "DetectivBD.db").end(num + 1)
                    if result == 0:
                        self.pixmap = QPixmap('мирныйМ.png')
                    else:
                        self.pixmap = QPixmap('бандитМ.png')
                    label.resize(70, 110)
                    label.setPixmap(self.pixmap)

            elif self.flag_day:
                self.flag_day = False
                self.textEdit.clear()
                if self.character1.life_check():
                    dialogue1 = self.character1.message(self.dead_list, 2)
                    self.textEdit.append(dialogue1)
                if self.character2.life_check():
                    dialogue2 = self.character2.message(self.dead_list, 2)
                    self.textEdit.append(dialogue2)
                if self.character3.life_check():
                    dialogue3 = self.character3.message(self.dead_list, 2)
                    self.textEdit.append(dialogue3)
                if self.character4.life_check():
                    dialogue4 = self.character4.message(self.dead_list, 2)
                    self.textEdit.append(dialogue4)
                if self.character5.life_check():
                    dialogue5 = self.character5.message(self.dead_list, 2)
                    self.textEdit.append(dialogue5)
                if self.character6.life_check():
                    dialogue6 = self.character6.message(self.dead_list, 2)
                    self.textEdit.append(dialogue6)
                if self.character7.life_check():
                    dialogue7 = self.character7.message(self.dead_list, 2)
                    self.textEdit.append(dialogue7)
                if self.character8.life_check():
                    dialogue8 = self.character8.message(self.dead_list, 2)
                    self.textEdit.append(dialogue8)
                if self.character9.life_check():
                    dialogue9 = self.character9.message(self.dead_list, 2)
                    self.textEdit.append(dialogue9)
                if self.character10.life_check():
                    dialogue10 = self.character10.message(self.dead_list, 2)
                    self.textEdit.append(dialogue10)
                attack_list = [[], [], [], [], [], [], [], [], [], []]
                con = sqlite3.connect("DetectivBD.db")
                cur = con.cursor()
                for i in range(1, 11):
                    if i not in self.dead_list:
                        a = """SELECT * FROM character WHERE id = {}""".format(i)
                        result = cur.execute(a).fetchall()
                        for elem in result:
                            attack_list[elem[1] - 1].append(str(elem[0]))
                con.close()
                con = sqlite3.connect("DetectivBD.db")
                cur = con.cursor()
                for i in range(1, 11):

                    if len(attack_list[i - 1]) > 0 and i not in self.dead_list:
                        a = """UPDATE character SET attack = \"{}\" WHERE id = {}""".format(
                            " ".join(attack_list[i - 1]), i)
                        result = cur.execute(a)
                        con.commit()
                con.close()
                self.textEdit.append("\n")
                self.flag = True
                self.textEdit.append("Нажмити клавишу C если хотите проверить игрока")
                self.textEdit.append("Нажмите клавишу K если хотите убить игрока")
        if event.key() == Qt.Key_P:
            MyWidget().end()


    def game(self):
        con = sqlite3.connect("DetectivBD.db")  # чистка таблицы БД
        cur = con.cursor()
        result = cur.execute("""DELETE from character""").fetchall()
        con.commit()
        con.close()

        self.dead_list = []
        self.flag = True
        self.flag_night = False
        self.flag_day = False
        self.game_ower.setText("")
        self.game_ower.setStyleSheet("background-color: ;color: ")

        for label in self.labels[:10]:
            self.pixmap = QPixmap('ДетективМ.png')
            label.resize(70, 110)
            label.setPixmap(self.pixmap)
        self.char_numders = [i for i in range(1, 11)]
        random.shuffle(self.char_numders)
        self.char_numders = self.char_numders[:3]
        if 1 in self.char_numders:
            self.character1 = Character(1, 1, self.char_numders)
        else:
            self.character1 = Character(0, 1, self.char_numders)
        if 2 in self.char_numders:
            self.character2 = Character(1, 2, self.char_numders)
        else:
            self.character2 = Character(0, 2, self.char_numders)
        if 3 in self.char_numders:
            self.character3 = Character(1, 3, self.char_numders)
        else:
            self.character3 = Character(0, 3, self.char_numders)
        if 4 in self.char_numders:
            self.character4 = Character(1, 4, self.char_numders)
        else:
            self.character4 = Character(0, 4, self.char_numders)
        if 5 in self.char_numders:
            self.character5 = Character(1, 5, self.char_numders)
        else:
            self.character5 = Character(0, 5, self.char_numders)
        if 6 in self.char_numders:
            self.character6 = Character(1, 6, self.char_numders)
        else:
            self.character6 = Character(0, 6, self.char_numders)
        if 7 in self.char_numders:
            self.character7 = Character(1, 7, self.char_numders)
        else:
            self.character7 = Character(0, 7, self.char_numders)
        if 8 in self.char_numders:
            self.character8 = Character(1, 8, self.char_numders)
        else:
            self.character8 = Character(0, 8, self.char_numders)
        if 9 in self.char_numders:
            self.character9 = Character(1, 9, self.char_numders)
        else:
            self.character9 = Character(0, 9, self.char_numders)
        if 10 in self.char_numders:
            self.character10 = Character(1, 10, self.char_numders)
        else:
            self.character10 = Character(0, 10, self.char_numders)

        dialogue1 = self.character1.message(self.dead_list)
        dialogue2 = self.character2.message(self.dead_list)
        dialogue3 = self.character3.message(self.dead_list)
        dialogue4 = self.character4.message(self.dead_list)
        dialogue5 = self.character5.message(self.dead_list)
        dialogue6 = self.character6.message(self.dead_list)
        dialogue7 = self.character7.message(self.dead_list)
        dialogue8 = self.character8.message(self.dead_list)
        dialogue9 = self.character9.message(self.dead_list)
        dialogue10 = self.character10.message(self.dead_list)
        attack_list = [[], [], [], [], [], [], [], [], [], []]
        con = sqlite3.connect("DetectivBD.db")
        cur = con.cursor()
        for i in range(1, 11):
            if i not in self.dead_list:
                a = """SELECT * FROM character WHERE id = {}""".format(i)
                result = cur.execute(a).fetchall()

                # Вывод результатов на экран
                for elem in result:
                    attack_list[elem[1] - 1].append(str(elem[0]))
        con.close()

        con = sqlite3.connect("DetectivBD.db")
        cur = con.cursor()
        for i in range(1, 11):

            if len(attack_list[i - 1]) > 0 and i not in self.dead_list:
                a = """UPDATE character SET attack = \"{}\" WHERE id = {}""".format(" ".join(attack_list[i - 1]), i)
                result = cur.execute(a)
                con.commit()
        con.close()

        self.textEdit.clear()

        self.textEdit.append(dialogue1 + "\n" + dialogue2 + "\n" + dialogue3 + "\n" + dialogue4)
        self.textEdit.append(dialogue5 + "\n" + dialogue6 + "\n" + dialogue7 + "\n" + dialogue8)
        self.textEdit.append(dialogue9 + "\n" + dialogue10 + "\n")
        self.textEdit.append("Нажмити клавишу C если хотите проверить игрока")
        self.textEdit.append("Нажмите клавишу K если хотите убить игрока")



app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
