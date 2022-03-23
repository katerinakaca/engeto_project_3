from bs4 import BeautifulSoup
import requests
import csv


# odkaz_na_kod = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=7&xnumnuts=5101"
nazev_obce = "Doksy"
soubor_csv = "vysledky_doksy.csv"
odkaz = "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=7&xobec=561495&xvyber=5101"
html = requests.get(odkaz)
soup = BeautifulSoup(html.text, "html.parser")
tabulka_1 = soup.find("table", {"id": "ps311_t1"})
list_1 = tabulka_1.find_all("td", {"class": "cislo"})
tabulka_2 = soup.find_all("td", {"class": "overflow_name"})
volici_v_seznamu = list_1[3].get_text()
vydane_obalky = list_1[4].get_text()
platne_hlasy = list_1[7].get_text()


print(platne_hlasy)







# def najit_kod_obce(odkaz_na_kod, nazev_obce):
#     kod = requests.get(odkaz_na_kod)
#     soup = BeautifulSoup(kod.text, "html.parser")
#     vsechny_td = soup.find_all("td", {"class": "overflow_name"})
#     spravny_tag = []
#     print(vsechny_td)
#     # for tr in vsechny_tr: