
# Vorgehensweise

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

Und im Browser [http://localhost:8080/hello](http://localhost:8080/hello)


(Rückfragen an Kristian: krother@academis.eu)
