"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Jan Černý
email: JohnyBgoode@seznam.cz
discord: JohnyBgoode84
"""


import sys
import csv
import requests
from bs4 import BeautifulSoup


# POMOCNÉ PROMĚNNÉ
title = ["Číslo", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy"]
url_main = "https://volby.cz/pls/ps2017nss/"
num_codes = []
name_locations = []
complete_list = []
political_parties_list = []

# KONTROLA ARGUMENTŮ
def input_arguments():
    arguments = sys.argv
    if len(arguments) != 3:
        print("Chybný počet parametrů. Zadejte prosím odkaz na webové stránky voleb a název výstupního souboru s příponou .csv!")
        sys.exit(1)

    url_argument = arguments[1]
    file_csv_argument = arguments[2]

    if not url_argument.startswith("https://volby.cz/pls/ps2017nss/"):
        print("Na první pozici musí být odkaz na webové stránky voleb!")
        sys.exit(1)
    elif not file_csv_argument.endswith(".csv"):
        print("Na druhé pozici musí být název výstupního souboru s příponou .csv !")
        sys.exit(1)

    return url_argument, file_csv_argument

# ZÍSKÁNÍ A ULOŽENÍ VŠECH MĚST Z DANÉHO OKRESU
def load_locations(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    cities = soup.find_all(class_="cislo")
    cities_names = soup.find_all(class_="overflow_name")
    for i in cities:
        temp = []
        code_cities = i.getText()
        link_cities = url_main + i.find("a").get("href")
        temp.append(code_cities)
        temp.append(link_cities)
        num_codes.append(temp)

    for i in cities_names:
        name_city = i.getText()
        name_locations.append(name_city)

# ZÍSKÁNÍ POTŘEBNÝCH DAT PRO KAŽDÉ MĚSTO Z VYBRANÉHO OKRESU
def get_political_parties(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    strany = soup.find_all(class_="overflow_name")
    for s in strany:
        political_parties_list.append(s.getText())

def get_result_pg_data(url):
    temp = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    voters = soup.find(class_="cislo", headers="sa2").getText()
    temp.append(int(voters.replace(u'\xa0', '')))
    envelopes_sub = soup.find(class_="cislo", headers="sa3").getText()
    temp.append(int(envelopes_sub.replace(u"\xa0", "")))

    valid_votes = soup.find(class_="cislo", headers="sa6").getText()
    temp.append(int(valid_votes.replace(u"\xa0", "")))

    for x in range(1, 4):
        try:
            strany_pocty = soup.find_all(class_="cislo", headers=f"t{x}sa2 t{x}sb3")
            for sp in strany_pocty:
                cislo = sp.getText()
                temp.append(int(cislo.replace(u"\xa0", "")))
        except:
            pass
    return temp

# STAŽENÍ DAT PRO JEDNOTLIVÉ MĚSTA
def download_data():
    print("Stahuji data... čekejte prosím.")
    cities_list = []
    get_political_parties(num_codes[1][1])
    for i in range(0, len(num_codes)):
        detail = []
        cities_list.extend(num_codes[i])
        cities_list.pop(1)  # odstraneni http odkazu na obec

        detail = get_result_pg_data(num_codes[i][1])
        cities_list.append(name_locations[i])
        cities_list.extend(detail)
        complete_list.append(cities_list)
        cities_list = []

# ULOŽENÍ STAŽENÝCH VÝSLEDKŮ DO SOUBORU
def save_data(save_file):
    temp = []
    temp.extend(title)
    temp.extend(political_parties_list)
    print(f"Ukladám data do souboru pod názvem \"{save_file}\".")
    with open(save_file, "w", newline='', encoding='utf-8') as file:
        wr = csv.writer(file)
        wr.writerow(temp)
        wr.writerows(complete_list)
    print(f"Data byla uložena.")

# MAIN PROGRAM
def get_all_data():
    url, file = input_arguments()
    load_locations(url)
    download_data()
    save_data(file)

if __name__ == "__main__":
    get_all_data()