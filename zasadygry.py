# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zasadygry.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Zasady_gry(object):
    def setupUi(self, Zasady_gry):
        Zasady_gry.setObjectName("Zasady_gry")
        Zasady_gry.resize(859, 735)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../npgwisielec/hangman.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Zasady_gry.setWindowIcon(icon)
        self.zasadylabel = QtWidgets.QLabel(Zasady_gry)
        self.zasadylabel.setGeometry(QtCore.QRect(30, 140, 801, 511))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.zasadylabel.setFont(font)
        self.zasadylabel.setObjectName("zasadylabel")
        self.koniecwbtn = QtWidgets.QPushButton(Zasady_gry)
        self.koniecwbtn.setGeometry(QtCore.QRect(700, 670, 75, 23))
        self.koniecwbtn.setObjectName("koniecwbtn")
        self.label = QtWidgets.QLabel(Zasady_gry)
        self.label.setGeometry(QtCore.QRect(300, 40, 291, 91))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 127);")
        self.label.setObjectName("label")

        self.retranslateUi(Zasady_gry)
        QtCore.QMetaObject.connectSlotsByName(Zasady_gry)

    def retranslateUi(self, Zasady_gry):
        _translate = QtCore.QCoreApplication.translate
        Zasady_gry.setWindowTitle(_translate("Zasady_gry", "Zasady Gry"))
        self.zasadylabel.setText(_translate("Zasady_gry", "Użytkowniku witaj w grze Wisielec!!!\n"
"Oto krótki opis przebiegu rozgrywki:\n"
"Na początku zostaniesz poproszony o wybór kategorii hasła oraz poziomu trudności.\n"
"Po dokonaniu wyboru i naciśnięciu przycisku \"Rozpocznij grę!\" ukaże się na ekranie zakodowane hasło.\n"
"Dostaniesz dziesięć żyć oraz zostaniesz poproszony o podanie litery.\n"
"Jeśli Twoja litera wystąpi w haśle przynajmniej raz zakodowane pola zostaną nią zastąpione na przykład:\n"
"    Hasło: P _ _ _ _ _ R\n"
"    Podaję literę \"O\"\n"
"    Hasło: P O _ _ _ O R\n"
"W przeciwnym wypadku utracisz życie. Dodatkowo dodane zostaną również punkty za każdą odgadniętą literę. \n"
"Gra się kończy gdy odgadniesz wszystkie litery lub stracisz wszystkie życia.\n"
"Na koniec ukaże się również twój wynik który zostanie uzależniony od poziomu trudności który wybrałeś.\n"
"(Więcej na ten temat poniżej)\n"
"\n"
"Życzymy miłej zabawy :)\n"
"\n"
"\n"
"====================================================================================\n"
"\n"
"Na początku gry gracz posiada 0 punktów, za każdą błędną odpowiedź traci 100 punktów, a za poprawną zdobywa 500.\n"
"Po zakończeniu rozgrywki wynik zostaje pomnożony przez współczynnik zależny od poziomu.\n"
"\n"
"Współczynniki dla odpowiednich poziomów:\n"
"Łatwy:  1.0\n"
"Średni: 3.0\n"
"Trudny: 5.0"))
        self.koniecwbtn.setText(_translate("Zasady_gry", "Koniec"))
        self.label.setText(_translate("Zasady_gry", "  Zasady Gry"))
        self.koniecwbtn.clicked.connect(self.zamknij)


    def zamknij(self):
        exit()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Zasady_gry = Ui_Zasady_gry()
    ui = Ui_Zasady_gry()
    Zasady_gry.show()
    sys.exit(app.exec_())
