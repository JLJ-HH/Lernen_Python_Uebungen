# ==============================================================================
# Modul 1.2 - Der große Praxis-Mix: 6 eigenständige Programmier-Challenges
# Datei: C:\Lernen_Python\01_grundlagen\bedingungen\06_praxis_mix.py
# ==============================================================================
# In dieser Datei gibt es kein Vorkauen mehr!
# Du wendest dein gesamtes Wissen selbstständig an:
# - Datentypen: int, float, bool, str
# - Bedingungen: if, elif, else
# - Logik-Operatoren: and, or
# - Dynamische Ausgaben: f-Strings
# - Logik umkehren (Fehler zuerst abfangen)
# ==============================================================================


# ------------------------------------------------------------------------------
# AUFGABE 1: Server-Latenz (Typ float mit Klassifizierung)
# Szenario:
# Ein Netzwerk-Monitoring misst den Ping (Reaktionszeit) zu einem Server in Millisekunden.
# - Unter 30.0 ms: "Perfekte Verbindung"
# - 30.0 bis unter 100.0 ms: "Gute Verbindung"
# - Ab 100.0 ms: "Schlechte Verbindung / Hohe Latenz"
#
# Deine Aufgabe:
# 1. Lege eine Variable 'ping_ms' an (teste z. B. 18.5, 45.0, 140.2).
# 2. Werte den Ping mit if / elif / else aus und gib die passende Meldung
#    inklusive des gemessenen Werts per f-String aus (z. B. "Gute Verbindung: 45.0 ms").
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 2: Zugriffskontrolle (Typ str mit 'or')
# Szenario:
# Ein Konfigurationsskript soll nur mit bestimmten Dateiformaten arbeiten.
# Erlaubt sind Dateien mit der Endung "json" ODER "yaml".
#
# Deine Aufgabe:
# 1. Lege eine Variable 'format' an (teste z. B. "json", "yaml" oder "xml").
# 2. Pruefe, ob das Format unterstuetzt wird:
#    - Wenn ja: Gib eine Erfolgsmeldung aus (z. B. "Format 'json' wird akzeptiert.").
#    - Sonst: Gib aus, dass das Format nicht unterstuetzt wird (z. B. "Format 'xml' nicht zulaessig!").
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 3: Produktions-Deployment (Typ bool und int mit 'and')
# Szenario:
# Ein Software-Release darf nur auf den Produktionsserver aufgespielt werden, wenn:
# - Alle Unit-Tests erfolgreich bestanden wurden ('tests_bestanden' ist True)
#   UND
# - Keine kritischen Sicherheitslücken offen sind ('offene_bugs' ist 0).
#
# Deine Aufgabe:
# 1. Lege zwei Variablen an: 'tests_bestanden' (Boolean) und 'offene_bugs' (Ganzzahl).
# 2. Pruefe mit 'and', ob beide Voraussetzungen gleichzeitig erfuellt sind:
#    - Wenn ja: Gib aus, dass das Release fuer den Deploy freigegeben ist.
#    - Sonst: Gib aus, dass das Release blockiert wird.
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 4: Der "Andersrum-Weg" (Ausschlusskriterien zuerst abfangen)
# Szenario:
# Ein Benutzer will an einem Geldautomaten 50 Euro abheben.
# Wir fangen zuerst die Fehler ab:
# 1. Ist die Karte gesperrt ('karte_gesperrt' ist True)? -> Abbruch: "Karte ist gesperrt!"
# 2. Ist nicht genug Geld auf dem Konto ('kontostand < abhebebetrag')? -> Abbruch: "Zu wenig Guthaben!"
# 3. Wenn kein Fehler vorliegt (else): Auszahlung genehmigen!
#
# Deine Aufgabe:
# 1. Lege drei Variablen an: 'karte_gesperrt' (bool), 'kontostand' (float) und 'abhebebetrag' (float).
# 2. Fange zuerst die Fehler ab und gib nur im Erfolgsfall das Geld aus.
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 5: Verschachtelte Paketstation (Nested if)
# Szenario:
# An einer Packstation moechte jemand ein Fach oeffnen:
# - Stufe 1: Zuerst wird der Abholcode geprueft ('code == 9876').
# - Stufe 2 (nur wenn Stufe 1 stimmt): Es wird geprueft, ob das Fach bezahlt ist ('bezahlt' ist True).
#
# Deine Aufgabe:
# Baue eine verschachtelte Bedingung:
# - Bei falschem Code: Sofort ausgeben "Falscher Abholcode!".
# - Bei richtigem Code, aber nicht bezahlt: Ausgeben "Bitte zuerst am Terminal bezahlen.".
# - Bei richtigem Code und bezahlt: Ausgeben "Fach 42 geoeffnet. Bitte Paket entnehmen!".
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 6: Das Finale: Cloud-Auto-Scaler (Typen-Mix, if / elif / else, and / or)
# Szenario:
# Ein Cloud-Server soll automatisch neue Instanzen starten (hochskalieren) oder
# Instanzen abschalten (herunterskalieren):
#
# Regel 1 ("Sofort hochskalieren"):
# CPU ueber 85.0 Prozent ODER RAM ueber 90.0 Prozent.
# -> Meldung ausgeben (z. B. "ALARM: Sofort neuen Server hinzuschalten!").
#
# Regel 2 ("Stromsparmodus / Runterskalieren"):
# CPU unter 20.0 Prozent UND RAM unter 30.0 Prozent.
# -> Meldung ausgeben (z. B. "Leerlauf erkannt: Server herunterfahren.").
#
# Regel 3 ("Normalbetrieb"):
# Alle anderen Faelle.
# -> Meldung ausgeben (z. B. "Systemauslastung im optimalen Bereich.").
#
# Deine Aufgabe:
# 1. Lege 'cpu' (float) und 'ram' (float) an.
# 2. Implementiere die 3 Regeln mit if / elif / else sowie 'and' und 'or'.
# ------------------------------------------------------------------------------

# Hier deinen Code schreiben:



print("=" * 60)

