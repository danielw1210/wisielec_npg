# -*- coding: utf-8 -*-

from peewee import *
import csv
import os.path
from wielecapp_ubuntu import *

baza_nazwa = 'wisielec_ubuntu.db'
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


class Ostatnia_gra(BaseModel):
    poziom = CharField()
    kategoria = CharField()
    haslo = CharField()


class Statystyka(BaseModel):
    nazwa_pola = CharField(null=False)
    ilosc = IntegerField()


#### koniec modelu ####


def czy_jest(plik):  # Funkcja sprawdza, czy plik istnieje na dysku
    if not os.path.isfile(plik):
        print("Plik {} nie istnieje!".format(plik))
        return False
    return True


def czytaj_dane(plik, separator=";"):  # funkcja odczytująca dane z lików csv
    dane = []  # pusta lista na rekordy

    if not czy_jest(plik):
        return dane

    with open(plik, 'r', newline='', encoding='utf-8') as plikcsv:
        tresc = csv.reader(plikcsv, delimiter=separator)
        for rekord in tresc:
            dane.append(rekord)
    return dane


def dodaj_dane(dane):  # funkcja dodająca dane odczytane z plików csv
    for model, plik in dane.items():
        pola = [pole for pole in model._meta.fields]
        pola.pop(0)  # usuwamy pola id
        wpisy = czytaj_dane(plik + '.csv', ';')
        model.insert_many(wpisy).execute()


def polacz():
    #####Trochę trzeba tu poprawić ####
    if os.path.exists(baza_nazwa):
        os.remove(baza_nazwa)
    baza.connect()  # połączenie z bazą
    baza.create_tables([Poziom, Kategoria, Haslo, Ostatnia_gra, Statystyka])  # tworzymy tabele

    dane = {
        Haslo: 'hasla',
        Poziom: 'poziomy',
        Kategoria: 'kategorie',
        Ostatnia_gra: 'ostatnia_gra',
        Statystyka: 'statystyka',
    }

    dodaj_dane(dane)
    baza.commit()
    baza.close()

    return True


def wykryj_poziom(that):  # funkcja zamieniająca nazwe poziomu (pobraną z comboboxa) na jego indeks
    if that.poziom_tr == "Łatwy":
        poz = 1
    elif that.poziom_tr == "Średni":
        poz = 2
    else:
        poz = 3
    return poz


def wykryj_kategorie(that):  # funkcja zamieniająca nazwe kategori (pobraną z comboboxa) na jej indeks
    if that.kategoria == "Geografia":
        kat = 1
    elif that.kategoria == "Jedzenie":
        kat = 2
    elif that.kategoria == "Kino":
        kat = 3
    elif that.kategoria == "Sport":
        kat = 4
    elif that.kategoria == "Nauka":
        kat = 5
    else:
        kat = 6
    return kat


def pobierz_haslo(that):  # funkcja wybierająca hasło o podanym poziomie i kategori z bazy danych
    haslo = Haslo.select(Haslo.haslo).where(Haslo.kategoria == wykryj_kategorie(that),
                                            Haslo.poziom == wykryj_poziom(that)).order_by(fn.Random()).scalar()
    return haslo


def odczytaj_gre(that):  # funkcja odczytująca stan ostaniej zapsanej gry
    poziom = Ostatnia_gra.select(Ostatnia_gra.poziom).scalar()
    kategoria = Ostatnia_gra.select(Ostatnia_gra.kategoria).scalar()
    haslo = Ostatnia_gra.select(Ostatnia_gra.haslo).scalar()
    return poziom, kategoria, haslo


def zapisz_gre(poziom, kategoria, haslo, that):  # funkcja zapisująca stan gry
    stare_dane = Ostatnia_gra.select().get()
    stare_dane.delete_instance()
    del stare_dane
    that.nowe_dane = Ostatnia_gra(poziom=poziom, kategoria=kategoria, haslo=haslo)
    that.nowe_dane.save()
    return "DONE"


def pobierz_statystyki(that):  # funkcja odczytująca statystyki gry
    wygrane = Statystyka.select(Statystyka.ilosc).where(Statystyka.nazwa_pola == 'WYGRANE').scalar()
    przegrane = Statystyka.select(Statystyka.ilosc).where(Statystyka.nazwa_pola == 'PRZEGRANE').scalar()
    return wygrane, przegrane


def aktualizuj_statystyki(wygrana, przegrana, that):  # funkcja aktualizująca statystyki gry
    dane = pobierz_statystyki(that)
    if wygrana == 1 and przegrana == 0:
        wyg = Statystyka.select().where(Statystyka.nazwa_pola == "WYGRANE").get()
        wyg.delete_instance()
        del wyg
        wygrana += dane[0]
        that.wygra = Statystyka(nazwa_pola="WYGRANE", ilosc=wygrana)
        that.wygra.save()

    elif wygrana == 0 and przegrana == 1:
        lose = Statystyka.select().where(Statystyka.nazwa_pola == "PRZEGRANE").get()
        lose.delete_instance()
        del lose
        przegrana += dane[1]
        that.przeg = Statystyka(nazwa_pola="PRZEGRANE", ilosc=przegrana)
        that.przeg.save()
    return "DONE"
