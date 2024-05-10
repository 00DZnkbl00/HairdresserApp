# Django AI  
Wymagania:
- python 3.10 (python --version)
- Django==4.0
- Pillow
- numpy
- pandas
- tensorflow==2.8.0
- tensorflow-hub
- protobuf==3.20

## Ustawienie środowiska
```sh
python -m venv .venv
```

### Założenie - pracuje na gitbash
```sh
source .venv\Scripts\activate
lub
source .venv/Scripts/activate
```
## Aktywacja zmiennej środowiskowej (Mac/Unix) 
### Założenie - pracuje na gitbash
```sh
source .venv/bin/activate
```

Jak jest aktywna wirtualna zmienna środowiskowa to przechodzimy do instalacji
(czyli w terminalu koło kursora jest w nawiasie .venv)

## Instalacja
```sh
pip install -r requirements.txt
```

### Sprawdzenie wersji Djando
```sh
python -m django --version
```

## Sworzenie projektu
```sh
django-admin startproject hairdresserBackend
```

# Uruchomienie
```sh
python hairdresserBackend/manage.py runserver
```
### Tworzenie własnej aplikacji
```sh
django-admin startapp reservationApp
```

# Migracje
```sh
 python hairdresserBackend/manage.py makemigrations
```
```sh
python hairdresserBackend/manage.py migrate
```

### Tworzenie superusera
```sh
python hairdresserBackend/manage.py createsuperuser
```
### admin zaq1@WSX