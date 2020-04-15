# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wisielecokno.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from baza_ubuntu import *
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(833, 612)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelwisielec = QtWidgets.QLabel(self.centralwidget)
        self.labelwisielec.setGeometry(QtCore.QRect(240, 40, 361, 111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelwisielec.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(60)
        font.setBold(False)
        font.setWeight(50)
        self.labelwisielec.setFont(font)
        self.labelwisielec.setStyleSheet("")
        self.labelwisielec.setTextFormat(QtCore.Qt.PlainText)
        self.labelwisielec.setObjectName("labelwisielec")
        self.rozpocznij_bnt = QtWidgets.QPushButton(self.centralwidget)
        self.rozpocznij_bnt.setGeometry(QtCore.QRect(330, 210, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rozpocznij_bnt.setFont(font)
        self.rozpocznij_bnt.setObjectName("rozpocznij_bnt")
        self.podaj_btn = QtWidgets.QLabel(self.centralwidget)
        self.podaj_btn.setGeometry(QtCore.QRect(80, 480, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.podaj_btn.setFont(font)
        self.podaj_btn.setObjectName("podaj_btn")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 260, 741, 201))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.hasloedt = QtWidgets.QTextEdit(self.frame)
        self.hasloedt.setGeometry(QtCore.QRect(113, 10, 571, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.hasloedt.setFont(font)
        self.hasloedt.setReadOnly(True)
        self.hasloedt.setObjectName("hasloedt")
        self.haslolabel = QtWidgets.QLabel(self.frame)
        self.haslolabel.setGeometry(QtCore.QRect(26, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.haslolabel.setFont(font)
        self.haslolabel.setObjectName("haslolabel")
        self.komunikatlabel = QtWidgets.QLabel(self.frame)
        self.komunikatlabel.setGeometry(QtCore.QRect(30, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.komunikatlabel.setFont(font)
        self.komunikatlabel.setObjectName("komunikatlabel")
        self.komunikatedt = QtWidgets.QTextEdit(self.frame)
        self.komunikatedt.setGeometry(QtCore.QRect(10, 110, 721, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.komunikatedt.setFont(font)
        self.komunikatedt.setReadOnly(True)
        self.komunikatedt.setObjectName("komunikatedt")
        self.koniec_btn = QtWidgets.QPushButton(self.centralwidget)
        self.koniec_btn.setGeometry(QtCore.QRect(720, 530, 111, 31))
        self.koniec_btn.setObjectName("koniec_btn")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 160, 801, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_kateg = QtWidgets.QLabel(self.layoutWidget)
        self.label_kateg.setMaximumSize(QtCore.QSize(101, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_kateg.setFont(font)
        self.label_kateg.setObjectName("label_kateg")
        self.horizontalLayout.addWidget(self.label_kateg)
        self.comboBox_kat = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_kat.setMaximumSize(QtCore.QSize(101, 16777215))
        self.comboBox_kat.setObjectName("comboBox_kat")
        self.comboBox_kat.addItem("")
        self.comboBox_kat.addItem("")
        self.comboBox_kat.addItem("")
        self.comboBox_kat.addItem("")
        self.comboBox_kat.addItem("")
        self.comboBox_kat.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_kat)
        self.label_poziom = QtWidgets.QLabel(self.layoutWidget)
        self.label_poziom.setMaximumSize(QtCore.QSize(181, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_poziom.setFont(font)
        self.label_poziom.setObjectName("label_poziom")
        self.horizontalLayout.addWidget(self.label_poziom)
        self.comboBox_pt = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_pt.setMaximumSize(QtCore.QSize(81, 16777215))
        self.comboBox_pt.setObjectName("comboBox_pt")
        self.comboBox_pt.addItem("")
        self.comboBox_pt.addItem("")
        self.comboBox_pt.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_pt)
        self.label_wynik = QtWidgets.QLabel(self.layoutWidget)
        self.label_wynik.setMaximumSize(QtCore.QSize(71, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_wynik.setFont(font)
        self.label_wynik.setObjectName("label_wynik")
        self.horizontalLayout.addWidget(self.label_wynik)
        self.wynik_edt = QtWidgets.QTextEdit(self.layoutWidget)
        self.wynik_edt.setMaximumSize(QtCore.QSize(111, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wynik_edt.setFont(font)
        self.wynik_edt.setToolTip("")
        self.wynik_edt.setReadOnly(True)
        self.wynik_edt.setObjectName("wynik_edt")
        self.horizontalLayout.addWidget(self.wynik_edt)
        self.podaj_edt = QtWidgets.QLineEdit(self.centralwidget)
        self.podaj_edt.setGeometry(QtCore.QRect(210, 480, 113, 31))
        self.podaj_edt.setObjectName("podaj_edt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionZapisz_gr = QtWidgets.QAction(MainWindow)
        self.actionZapisz_gr.setObjectName("actionZapisz_gr")
        self.actionWczytaj_gr = QtWidgets.QAction(MainWindow)
        self.actionWczytaj_gr.setObjectName("actionWczytaj_gr")
        self.actionStatystyki = QtWidgets.QAction(MainWindow)
        self.actionStatystyki.setObjectName("actionStatystyki")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.koniec_btn.clicked.connect(self.koniec)  # obsługa wcisniecia przycisku koniec
        self.rozpocznij_bnt.clicked.connect(self.rozpoczecie)  # obsluga wcisniecia przycisku rozpocznij gre
        self.ustaw_kat(self.comboBox_kat.currentText())  # ustawienie kategori poczatkowej
        self.comboBox_kat.activated[str].connect(self.ustaw_kat)  # obsluga ustawiania kategorii
        self.ustaw_pt(self.comboBox_pt.currentText())  # ustawienie poziomu tr. poczatkowego
        self.comboBox_pt.activated[str].connect(self.ustaw_pt)  # obsluga ustawianiapoziomu tr.
        self.podaj_edt.returnPressed.connect(self.odczytaj) #obsluga podawania liter
        self.wynik=None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wisielec"))
        self.labelwisielec.setText(_translate("MainWindow", "Wisielec"))
        self.rozpocznij_bnt.setText(_translate("MainWindow", "Rozpocznij grę!"))
        self.podaj_btn.setText(_translate("MainWindow", "Podaj literę:"))
        self.haslolabel.setText(_translate("MainWindow", "Hasło:"))
        self.komunikatlabel.setText(_translate("MainWindow", "Komunikat:"))
        self.koniec_btn.setText(_translate("MainWindow", "Koniec"))
        self.label_kateg.setText(_translate("MainWindow", "Kategoria:"))
        self.comboBox_kat.setItemText(0, _translate("MainWindow", "Geografia"))
        self.comboBox_kat.setItemText(1, _translate("MainWindow", "Jedzenie"))
        self.comboBox_kat.setItemText(2, _translate("MainWindow", "Kino"))
        self.comboBox_kat.setItemText(3, _translate("MainWindow", "Sport"))
        self.comboBox_kat.setItemText(4, _translate("MainWindow", "Nauka"))
        self.comboBox_kat.setItemText(5, _translate("MainWindow", "Zwierzęta"))
        self.label_poziom.setText(_translate("MainWindow", "Poziom trudności:"))
        self.comboBox_pt.setItemText(0, _translate("MainWindow", "Łatwy"))
        self.comboBox_pt.setItemText(1, _translate("MainWindow", "Średni"))
        self.comboBox_pt.setItemText(2, _translate("MainWindow", "Trudny"))
        self.label_wynik.setText(_translate("MainWindow", "Wynik:"))
        self.actionZapisz_gr.setText(_translate("MainWindow", "Zapisz grę"))
        self.actionWczytaj_gr.setText(_translate("MainWindow", "Wczytaj grę"))
        self.actionStatystyki.setText(_translate("MainWindow", "Statystyki"))

    def koniec(self):
        exit() #funkcjonalność przycisku koniec

    def rozpoczecie(self): #funkcja realizująca funkcjonalosc gry
        self.liczba_prob = 10
        self.wynik=0
        self.wylosowane_haslo = pobierz_haslo(self)
        self.komunikatedt.setText(str("Rozpoczęto grę na poziomie "+ self.poziom_tr + "m. Hasło z kategorii " + self.kategoria +" zostało wylosowane.\nPodaj pierwszą literę:\t\t\t\t Pozostało prób:" + str(self.liczba_prob)))
        self.hasloedt.setText(str(len(self.wylosowane_haslo)*'*  '))
        self.wynik_edt.setText(str(self.wynik))
        self.wykorzystane_litery=[]
        self.indeksy = []
        for i in range(len(self.wylosowane_haslo)):
            self.indeksy.append(False)

    def czy_wygrana(self): #fukcja sprawdzająca czy wszystkie litery zostały odgadnięte
        self.zgadniete = 0
        for i in range(len(self.wylosowane_haslo)):
            if self.indeksy[i]:
                self.zgadniete +=1
        if self.zgadniete == len(self.wylosowane_haslo):
            self.komunikatedt.setText("Gratulacje wygrałeś!!!\nTwój wynik końcowy: " + str(self.wynik_koncowy()))
            return True

    def wynik_koncowy(self):
        if self.poziom_tr == "Łatwy":
            return self.wynik
        elif self.poziom_tr == "Średni":
            return 3*self.wynik
        elif self.poziom_tr == "Trudny":
            return 5*self.wynik

    def odczytaj(self):  # funkcja odczytująca podawane litery
        self.podana_litera = self.podaj_edt.text().upper()
        if self.wynik != None and not self.czy_wygrana():
            if len(self.podana_litera)==1:
                if self.podana_litera in self.wylosowane_haslo and self.podana_litera not in self.wykorzystane_litery:
                    self.wykorzystane_litery.append(self.podana_litera)
                    self.wynik += 500
                    self.wynik_edt.setText(str(self.wynik))
                    self.komunikatedt.setText("Brawo! Zgadłeś! \t\t\t\t Pozostało prób:" + str(self.liczba_prob) +"\nWykorzystane litery:"+ str(self.wykorzystane_litery) +"\nPodaj następną literę: ")
                    for i in range(len(self.wylosowane_haslo)):
                        if self.wylosowane_haslo[i] == self.podana_litera:
                            self.indeksy[i] = True

                    haslo_kom = " ".join([litera if self.indeksy[i] else "*" for i, litera in enumerate(self.wylosowane_haslo)])
                    self.hasloedt.setText(haslo_kom.strip())
                    self.czy_wygrana()

                elif self.podana_litera in self.wykorzystane_litery:
                    self.komunikatedt.setText("Już podałeś tą literę!\t\t\t\t Pozostało prób:" + str(self.liczba_prob) +"\nWykorzystane litery:"+ str(self.wykorzystane_litery) +"\nPodaj następną literę: ")
                else:
                    self.wykorzystane_litery.append(self.podana_litera)
                    self.liczba_prob-=1
                    self.wynik-=100
                    self.komunikatedt.setText("Pudło!\t\t\t\t Pozostało prób:" + str(self.liczba_prob) +"\nWykorzystane litery:"+ str(self.wykorzystane_litery) +"\nPodaj następną literę: ")
                    self.wynik_edt.setText(str(self.wynik))
                    if self.liczba_prob==0:
                        self.komunikatedt.setText("GAME OVER")
            else:
                self.komunikatedt.setText("Wprowadzono błędne dane! Spróbuj ponownie")
            self.podaj_edt.setText("")
        else:
            self.komunikatedt.setText("Aby rozpocząć grę wybierz ustawienia i klknij Rozpocznij grę.")
            self.podaj_edt.setText("")

    def ustaw_kat(self,wartosc):  # funkcja wykrywa ustawienie innej kategorii niz poczatkowa(pierwsza w comboboxie)
        self.kategoria = wartosc

    def ustaw_pt(self,wartosc):  # funkcja wykrywa ustawienie innego poziou tr. niz poczatkowy(pierwsza w comboboxie)
        self.poziom_tr = wartosc



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    polacz()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

