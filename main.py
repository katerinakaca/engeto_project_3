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
    mesto = (mesto_list[2].get_text())[7:-1]
    kod_mesta = odkaz[-18:-12]
    kand_strany = list_kandidujicich_stran(tabulka_2)
    slovnik = {"kód obce": kod_mesta, "název obce": mesto, "voliči v seznamu":volici_v_seznamu, "vydané obálky": vydane_obalky, "platné hlasy": platne_hlasy, "kandidující strany": kand_strany}
    zapis_do_csv(soubor_csv, slovnik)

def list_kandidujicich_stran(tabulka_2):
    strany = []
    for strana in tabulka_2[:]:
        kand_strana = strana.get_text()
        strany.append(kand_strana)
    return strany

def zapis_do_csv(soubor_csv, slovnik):
    with open(soubor_csv, "w", encoding="utf-8") as soubor:
        writer = csv.writer(soubor)
        for klic in slovnik.items():
            writer.writerow(klic)
    print("Výsledky byly zapsány do souboru csv.")



if __name__ == "__main__":
    main(odkaz, soubor_csv)





