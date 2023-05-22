ELECTIONS SCRAPER - Třetí projekt Engeto Online Python Akademie.

# POPIS
Tento skript extrahuje ze všech měst z vybraného okresu výsledky z hlasování do Poslanecké směnovny Parlamentu České republiky, které proběhlo v roce 2017.
Po dokončení sriptu se vyextrahované data uloží do souboru o formátu csv.

Odkaz na výsledky voleb konané v roce 2017: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

# INSTALACE POTŘEBNÝCH KNIHOVEN
Potřebné knihovny, včetně verzí, naleznete v souboru "requirements.txt"

Je doporučeno použít nové virtuální prostředí a pomocí manažera spustit =

pip3 --version                    (ověření verze manažeru)
pip3 install -r requirements.txt  (nainstalování knihoven z txt souboru)
	

# SPUŠTĚNÍ
Pro spuštění programu je potřeba spustit soubor "projekt_3.py" a následně zadat dva povinné argumenty. 
1. argument = URL vybraného okresu
2. argument = Název výstupního souboru s příponou ".csv"

Pozn.: Pro spuštění využijeme příkazový řádek.

# UKÁZKA SPUŠTĚNÍ
Pro příklad níže jsou zvoleny výsledky do PS ze Semilského okresu

python projekt_3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=7&xnumnuts=5104" "vysledky_voleb_okres_semily.csv"

Poté se stáhnou data ze zadaného odkazu a uloží se do souboru s příponou ".csv".
