# -*- coding: utf-8 -*-

from peewee import *
import csv
import os.path
from wisielecapp_win import *

baza_nazwa = 'wisielec_win.db'
baza = SqliteDatabase(baza_nazwa)  # instancja bazy

#### Model ####
class BaseModel(Model):
    class Meta:
        database = baza


class Poziom(BaseModel):
    poziom = CharField(null=False)


class Kategoria(BaseModel):
    kategoria = CharField(null=False)


class Haslo(BaseModel):
    poziom = ForeignKeyField(Poziom, related_name='poziom')
    kategoria = ForeignKeyField(Kategoria, related_name='kategoria')
    haslo = CharField()

    class Meta:
        order_by = ('haslo',)

#### koniec modelu ####


def czy_jest(plik): #Funkcja sprawdza, czy plik istnieje na dysku
    if not os.path.isfile(plik):
        print("Plik {} nie istnieje!".format(plik))
        return False
    return True


def czytaj_dane(plik, separator=";"): #funkcja odczytująca dane z lików csv
    dane = []  # pusta lista na rekordy

    if not czy_jest(plik):
        return dane

    with open(plik, 'r', newline='', encoding='utf-8') as plikcsv:
        tresc = csv.reader(plikcsv, delimiter=separator)
        for rekord in tresc:
            dane.append(rekord)
    return dane


def dodaj_dane(dane): #funkcja dodająca dane odczytane z plików csv
    for model, plik in dane.items():
        pola = [pole for pole in model._meta.fields]
        pola.pop(0)  # usuwamy pola id
        wpisy = czytaj_dane(plik + '.csv', ';')
        model.insert_many(wpisy).execute()


def polacz():
    if os.path.exists(baza_nazwa):
        os.remove(baza_nazwa)
    baza.connect()  # połączenie z bazą
    baza.create_tables([Poziom, Kategoria, Haslo])  # tworzymy tabele

    dane = {
        Haslo: 'hasla',
        Poziom: 'poziomy',
        Kategoria: 'kategorie',
    }

    dodaj_dane(dane)
    baza.commit()
    baza.close()

    return True

def wykryj_poziom(that): #funkcja zamieniająca nazwe poziomu (pobraną z comboboxa) na jego indeks
    if that.poziom_tr == "Łatwy":
        poz = 1
    elif that.poziom_tr =="Średni":
        poz = 2
    else:
        poz = 3
    return poz

def wykryj_kategorie(that): #funkcja zamieniająca nazwe kategori (pobraną z comboboxa) na jej indeks
    if that.kategoria == "Geografia":
        kat = 1
    elif that.kategoria =="Jedzenie":
        kat = 2
    elif that.kategoria =="Kino":
        kat = 3
    elif that.kategoria =="Sport":
        kat = 4
    elif that.kategoria =="Nauka":
        kat = 5
    else:
        kat = 6
    return kat

def pobierz_haslo(that): #funkcja wybierająca hasło o podanym poziomie i kategori z bazy danych
    haslo = Haslo.select(Haslo.haslo).where(Haslo.kategoria == wykryj_kategorie(that), Haslo.poziom == wykryj_poziom(that)).order_by(fn.Random()).scalar()
    return haslo


def liczba_liter(that): #funkcja zwracająca liczbę liter w haśle
    haslo = pobierz_haslo(that)
    liczba_li = len(haslo)
    return liczba_li
