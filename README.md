**A website created with Python Bottle and SQLite for entering and showing numbers with a timestamp. Used at Lageso in Berlin for helping refugees in the German registration process**

# Problem

Um in Deutschland registriert zu werden, müssen Flüchtlinge zunächst eine Nummer bekommen. Wann diese aufgerufen wird, ist schwer abzuschätzen und bisher nur vor Ort erkennbar. Die Lösung ist eine Internetseite, auf der Nummern eingetragen und abgerufen werden können. [Hintergrundartikel]( http://www.taz.de/Wartezeiten-am-Berliner-Lageso/!5228958/)

## Nutzerkreis

Die Internetseite soll von Flüchtlingen, die sich im LaGeSO registrieren wollen, genutzt werden, um herauszufinden, ob ihre Nummer schon aufgerufen wurde. Bisher stehen dort täglich mehrere hundert Menschen in der Warteschlange, um dies vor Ort zu erfahren. Freiwillige tragen dabei die Nummern ein.

# Funktionen

## Bestehende Funktionen

0. Seite: Übersicht und Auswahlseite
1. Seite: Helfer steht am LaGeSo und gibt Nummern ein [_____] <diese werden mit timestamp in eine Tabelle geschrieben>
2. Seite: Flüchtling fragt ab: Wurde meine Nummer gezogen? [_____] => Antwort: X mal am LaGeSo eingetragen von (Erste Eintragung) DD.MM.YY hh bis DD.MM.YY hh (LetzteEintragung)

## Mögliche Erweiterungen 
Wir freuen uns über Beiträge, die unsere [Issues](https://github.com/fzesch/lagesonum/issues) behandeln oder lösen. Diese sind am dringendsten. 

Darüber hinaus gibt es größere Erweiterungen, die sinnvoll sind:
 
 - Email-Benachrichtigung wenn Nummer aufgerufen wird
 - Nutzerkonten mit Passwortverwaltung (oder Login über facebook)

# Umsetzung

Die <a href="https://docs.google.com/document/d/1g8qLax2ScIFKubpZzflVgdy8Kvilo0ga94eelDZ8U-M/edit#">Anforderungen sind in einem Google-Dokument detailliert</a>.

Die technische Umsetzung erfolgt mit dem Python-Webframework <a href="http://bottlepy.org/docs/dev/index.html">Bottle</a> und SQLite.

Es gibt eine [Anleitung, wie man das Projekt lokal zum Laufen bringt](https://github.com/fzesch/lagesonum/blob/master/LOG.md).

## i18n - Übersetzung und Internationalisierung
Umsetzung mit gettext und bottle_i18n

- Die Übersetzungen werden in einer Tabelle erstellt (Google-Docs)
    - Sprachen: Deutsch	English	Russian	French	Kurdisch	Arabisch	Türkisch	Farsi	Dari	Tigrinya	Italienisch	Esperanto Urdu	Dari	Portugiesisch	Albanisch	Bosnisch	Serbisch
- Mit dem Translate-Toolkit-csv2po machen wir .po-Dateien
- Aus den .po-Dateien werden .mo-Dateien erzeugt, die bottle_i18n dann verwenden kann
Deployment muss besser skalieren können, s. [Issue #7](https://github.com/fzesch/lagesonum/issues/7)

## Konfiguration

Die Umgebungsvariable `$PYHTONPATH` muß auf das Hauptverzeichnis des Projekts gesetzt sein (welches die Ordner `lagesonum` und `tests` enthält).

Die Paketabhängigkeiten befinden sich in der Datei `requirements.txt`. Installation mit 

    pip install -r requirements.txt

## Unit Tests

Funktionieren mit Python `unittest`:

    python tests/


# Kontakt

f.zesch@mailbox.org
