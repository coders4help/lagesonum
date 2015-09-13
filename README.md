**A website created with Python Bottle and SQLite for entering and showing numbers with a timestamp. Used at Lageso in Berlin for helping refugees in the German registration process**

# Problem

Um in Deutschland registriert zu werden, müssen Flüchtlinge zunächst eine Nummer bekommen. Wann diese aufgerufen wird, ist schwer abzuschätzen und bisher nur vor Ort erkennbar. Die Lösung ist eine Internetseite, auf der Nummern eingetragen und abgerufen werden können. (Hintergrundartikel: http://www.taz.de/Wartezeiten-am-Berliner-Lageso/!5228958/)

## Nutzerkreis

Die Internetseite soll von Flüchtlingen, die sich im LaGeSO registrieren wollen, genutzt werden, um herauszufinden, ob ihre Nummer schon aufgerufen wurde. Bisher stehen dort täglich mehrere hundert Menschen in der Warteschlange, um dies vor Ort zu erfahren. Freiwillige tragen dabei die Nummern ein.

# Funktionen

## Bestehende Funktionen

1.Seite: Helfer steht am LaGeSo und gibt Nummern ein [_____] <diese werden mit timestamp in eine Tabelle geschrieben>
2. Seite: Flüchtling fragt ab: Wurde meine Nummer gezogen? [_____] => Antwort: X mal am LaGeSo eingetragen von (Erste Eintragung) DD.MM.YY hh bis DD.MM.YY hh (LetzteEintragung)

## Mögliche Erweiterungen --> Bitte helfen

 - 3. Seite nice to have: Leaderboard: X verifizierte Nummern eingetragen (verifiziert = von 3 oder mehr unabhängigen Leuten eingetragen)
 - Feature nice to have: SMS, Email, Push, Whatsapp Benachrichtigung wenn Nummer aufgerufen wird
 - Nutzerkonten mit Passwortverwaltung (oder Login über facebook)
 - Skalierung über mehrere Orte (die man aus Liste auswählen kann)
 - Vorschlagen von neuen Orten (händische Bestätigung von Administrator in Admin-View)
 - Internationalisierung

# Umsetzung

Die <a href="https://docs.google.com/document/d/1g8qLax2ScIFKubpZzflVgdy8Kvilo0ga94eelDZ8U-M/edit#">Anforderungen sind in einem Google-Dokument detailliert</a>.

Die technische Umsetzung erfolgt mit dem Python-Webframework <a href="http://bottlepy.org/docs/dev/index.html">Bottle</a> und SQLite.
