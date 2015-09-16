# Lokal zum Laufen bringen

- git clone git@github.com:fzesch/lagesonum.git
- cd lagesonum
- sudo pip install bottle              # recommended
- sudo easy_install bottle             # alternative without pip
- sudo apt-get install python-bottle   # works for debian, ubuntu, ...
- pip install -r requirements.txt
- python lagesonum

# Vorgehensweise zum Erstellen des Projekts

## 1. Grundstruktur mit pyscaffold angelegt

    pyscaffold -p lagesonum

## 2. virtualenv Umgebung angelegt (benutzt `virtualenvwrapper`)

    mkvirtualenv lagesonum
    setvirtualenvproject ~/.virtualenvs/lagesonum/ .

## 3. bottle installiert

    pip install bottle


## 4. Abhängigkeiten installiert

    pip freeze > requirements.txt

so daß woanders alles auf einmal installiert werden kann:

    pip install -r requirements.txt


## 5. Hello World aus der Bottle-Dokumentation ausprobiert

funktionieren sollte:

    python lagesonum    

Und im Browser [http://localhost:8080/](http://localhost:8080/)

## 6. Deployment auf PythonAnywhere

1. Account auf [https://www.pythonanywhere.com](https://www.pythonanywhere.com) anlegen
2. Web-App `lagesonum` mit Bottle und Python 3.4 anlegen
3. Konsole (Bash) auf PythonAnywhere starten
4. `git clone https://github.com/fzesch/lagesonum.git`

Es sind kleine Verrenkungungen wie das Verschieben von Dateien nötig, da das Verzeichnis `lagesonum` bereits existiert. Ich habe alles so arrangiert, daß `bottle_app.py` aus dem Repository an der gleichen Stelle landet wie die von PythonAnywhere angelegte Datei mit diesem Namen. Das geht sicher noch eleganter.


(Rückfragen an Kristian: krother@academis.eu)
