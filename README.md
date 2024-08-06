# Uber Statistics

## Introducere

Aplicatia va genera statistici despre cursele unui utilizator de Uber.
Aplicatia va primi un fisier din linia de comanda, pe care il va procesa si pe baza informatiilor primite va afisa in terminal diferite informatii:
- Total bani cheltuiti;
- Total curse(completed, canceled);
- Total curse per an;
- Total curse per oras;
- Total curse per luna;
- Distanta totala (in km);
- Curse per produs(UberX, Comfort, Black);
- Perioada totala petrecuta in curse(secunde, minute, ore, zi);
- Cea mai scurta cursa (in minute);
- Cea mai lunga cursa (in minute).

## Instalare

Cloneaza repozitory-ul:
https://github.com/Cata341/Proiect-1.git
Navigheaza in folderul proiectului.
Creaza un virtual environment si instaleaza dependintele
cd proiect1-curs
python -m venv venv
pip install -r requirements.txt

## Requirements
- numpy;
- pandas;
- python-dateutil;
- pytz;
- six;
- tzdata.

## Utilizare
- Deschide un terminal de comanda;
- Activeaza virtual environment-ul creat anterior;
- Cu venv activat introducem comanda:
python script.py trips_data.1.csv
