Název projektu

Objednávkový systém autosalonu


Autor

Jméno a příjmení: Tomáš Kopecký
E-mail: kopecky4@spsejecna.cz
Škola: (název školy)


Popis projektu

Tento projekt je školní databázová aplikace vytvořená v jazyce Python.
Aplikace slouží ke správě zákazníků, automobilů, výbavy a objednávek v autosalonu.

Projekt využívá relační databázi MySQL a návrhový vzor Repository pattern (D1).
Aplikace umožňuje práci s databází, import dat, transakce a generování reportů.


Použité technologie

Python 3.10+

MySQL Server

mysql-connector-python


Struktura projektu
autosalon/
├── main.py                # hlavní spouštěcí soubor
├── db.py                  # připojení k databázi
├── repositories/          # repository vrstvy
├── services/              # aplikační logika (import, reporty)
├── config/
│   └── config.ini         # konfigurace databáze
├── data/                  # importní soubory (CSV, JSON)
├── doc/                   # dokumentace projektu
├── autosalon.sql          # SQL export databáze
└── README.txt


Požadavky na spuštění

Nainstalovaný Python 3.10 nebo novější

Nainstalovaný MySQL Server

Přístup k příkazové řádce

Instalace databáze

Spusťte MySQL klienta

Vytvořte databázi:

CREATE DATABASE autosalon;


Přepněte se do databáze:

USE autosalon;


Importujte databázi:

SOURCE autosalon.sql;

Konfigurace aplikace

Otevřete soubor:

config/config.ini


a nastavte přihlašovací údaje k databázi:

[database]
host = localhost
port = 3306
user = root
password = heslo
database = autosalon

Instalace závislostí

V příkazové řádce spusťte:

pip install mysql-connector-python

Spuštění aplikace

Aplikaci spustíte příkazem:

python main.py


Po spuštění se zobrazí textové menu, pomocí kterého lze aplikaci ovládat.

Funkce aplikace

přidání, úprava a smazání zákazníka

přidání, úprava a smazání automobilu

přidání výbavy

vytvoření objednávky (práce s více tabulkami)

import dat z CSV a JSON

generování souhrnného reportu

ošetření chybových stavů


Import dat

Aplikace umožňuje import:

zákazníků ze souboru CSV

automobilů ze souboru JSON

Importní soubory se nachází ve složce /data.


Chybové stavy

Aplikace ošetřuje:

chybné připojení k databázi

neexistující soubory

neplatné vstupy uživatele

chyby konfigurace

Při chybě je uživatel informován pomocí chybové hlášky.


Testování

Součástí projektu jsou tři testovací scénáře ve formátu PDF, které popisují:

instalaci a spuštění aplikace

běžnou práci s aplikací

chybové stavy, import a reporty


Závěr

Projekt splňuje všechny požadavky zadání a je připraven k testování a odevzdání.