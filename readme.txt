README.txt
Aplikacja webowa tworząca listę obecności na wykładzie - opis konfiguracji środowiska 

Opis Projektu:
Projekt ten jest systemem rejestracji obecności opartym na frameworku Flask w języku Python. Aplikacja wykorzystuje bazę danych MySQL do przechowywania informacji o studentach oraz wykładowcach.

Wymagane Technologie:
Python: 3.10.12
Flask: 3.0.0
MySQL: 8.0.35

Instrukcje Uruchomienia:
Upewnij się, że masz zainstalowanego Pythona na swoim systemie. Możesz go pobrać ze strony https://www.python.org/downloads/.

Zainstaluj narzędzie pip, jeśli jeszcze nie jest zainstalowane. Możesz to zrobić, wykonując poniższe polecenie w terminalu:

sudo apt update
sudo apt install python3-pip

Zainstaluj narzędzie virtualenv, które pozwoli na utworzenie izolowanego środowiska projektu:

pip3 install virtualenv

Utwórz nowe środowisko w katalogu projektu:

virtualenv venv

Aktywuj środowisko:

source venv/bin/activate

Dla systemu Windows:

.\venv\Scripts\activate

Zainstaluj zależności projektu z pliku requirements.txt z folderu server, używając poniższego polecenia w terminalu:

pip install -r requirements.txt

Utwórz bazę danych MySQL o nazwie agh_db korzystając z pliku sql znajdującego się w folderze database.

W pliku app.py ustaw odpowiednie dane do połączenia z bazą danych:


connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='agh_db'
)

Uruchom aplikację, wpisując w terminalu:

flask run 

Otwórz przeglądarkę i przejdź do http://localhost:5000/ aby korzystać z aplikacji.

Strony Aplikacji:

Strona Główna

Adres: http://localhost:5000/
Wyświetla witrynę główną aplikacji.

Rejestracja Obecności

Adres: http://localhost:5000/presence
Pozwala studentom zarejestrować swoją obecność.

Logowanie

Adres: http://localhost:5000/login
Strona logowania dla wykładowców.

Tabela Obecności

Adres: http://localhost:5000/table_presence
Wyświetla tabelę z danymi studentów.

Wylogowanie

Adres: http://localhost:5000/logout
Wylogowuje z systemu.

Autor:
Tomasz Wesołek
