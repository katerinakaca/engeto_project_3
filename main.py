from bs4 import BeautifulSoup
import requests
import csv

soubor_csv = "vysledky_doksy.csv"
odkaz = "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=7&xobec=561495&xvyber=5101"

if "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=" and "obec=" and "vyber=" not in odkaz:
    print("Zadali jste špatný internetový odkaz, prosím postupujte přesně podle návodu v READ.ME.")
    exit()

def main(odkaz: str, soubor_csv: str):
    html = requests.get(odkaz)
    soup = BeautifulSoup(html.text, "html.parser")
    tabulka_1 = soup.find("table", {"id": "ps311_t1"})
    list_1 = tabulka_1.find_all("td", {"class": "cislo"})
    tabulka_2 = soup.find_all("td", {"class": "overflow_name","headers":"t1sa1 t1sb2"})
    # list_2 = tabulka_2.get_text()
    tabulka_mesto = soup.find("div", {"id": "publikace", "class": "topline"})
    mesto_list = tabulka_mesto.find_all("h3")
    volici_v_seznamu = list_1[3].get_text()
    vydane_obalky = list_1[4].get_text()
    platne_hlasy = list_1[7].get_text()
    mesto = (mesto_list[2].get_text())[7:]
    kod_mesta = odkaz[-18:-12]
    kand_strany = list_kandidujicich_stran(tabulka_2)
    print(
        f"""
        volici v seznamu: {volici_v_seznamu}
        vydane obalky: {vydane_obalky}
        platne hlasy: {platne_hlasy}
        mesto: {mesto}
        kod mesta: {kod_mesta}
        kand strany: {kand_strany}
    """)


def list_kandidujicich_stran(tabulka_2):
    strany = []

    for strana in tabulka_2[:]:
        kand_strana = strana.get_text()
        strany.append(kand_strana)
    return strany

def zapis_do_csv():
    print("zapsano")

main(odkaz, soubor_csv)