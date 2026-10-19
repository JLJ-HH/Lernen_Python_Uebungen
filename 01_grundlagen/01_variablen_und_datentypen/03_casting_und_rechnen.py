# ==============================================================================
# Modul 1.1: Grundlagen - Type-Casting & Rechnen
# Datei: 03_casting_und_rechnen.py
# ==============================================================================

# [WARUM MUSS MAN DATENTYPEN UMWANDELN?]
# Haeufig kommen Daten aus Eingabefeldern oder APIs als Text (str) an.
# Mit Text kann Python aber nicht rechnen!
#
# Was passiert ohne Umwandlung?
#   "10" + "10"  --> ergibt "1010"  (Text wird nur aneinandergehaengt!)
#    10  +  10   --> ergibt 20      (echte mathematische Addition)
#
# "Type-Casting" bedeutet: Wir verwandeln einen Typ gezielt in einen anderen:
# - int("1250")    -> verwandelt den Text "1250" in die ganze Zahl 1250
# - float("150.0") -> verwandelt den Text "150.0" in die Kommazahl 150.0
# - str(100)       -> verwandelt die Zahl 100 in den Text "100"
# - bool(1)        -> verwandelt Zahlen/Werte in True (0 oder "" wird False)

# ==============================================================================
# [DAS MUSTERBEISPIEL: CASTING & RECHNEN]
# ==============================================================================

# 1. Eine Zahl liegt als Text vor:
eingabe_text = "50"

# 2. In eine ganze Zahl (int) umwandeln (Casting):
zahl = int(eingabe_text)

# 3. Jetzt koennen wir mathematisch rechnen (Beispiel: wir rechnen 25 dazu):
ergebnis = zahl + 25

# 4. Ergebnis und Datentyp pruefen:
print(ergebnis)         # Gibt 75 aus
print(type(ergebnis))   # Gibt <class 'int'> aus

print("=" * 60)


# ==============================================================================
# [DEINE 6 PRAXIS-AUFGABEN]
# Ziel: Umwandeln und Rechnen trainieren 
# ==============================================================================

# ------------------------------------------------------------------------------
# AUFGABE 1: KI-Token-Verbrauch berechnen
# Ein Sprachmodell hat 1250 Token verbraucht. Der Wert kommt als Text an.
# 1. Wandle 'token_str' mit int() in eine Ganzzahl um.
# 2. Ein neuer Prompt verbraucht zusaetzlich 350 Token. Berechne die Gesamtzahl.
# 3. Gib das Ergebnis mit print() aus.
# 4. Gib den Datentyp des Ergebnisses mit print(type(...)) aus.
# ------------------------------------------------------------------------------

token_str = "1250"

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 2: Speicherplatz-Berechnung
# Ein Backup belegt aktuell 45.8 Gigabyte. Der Wert kommt als Text an.
# 1. Wandle 'speicher_str' mit float() in eine Kommazahl um.
# 2. Durch Bereinigung werden 12.3 Gigabyte frei. Ziehe 12.3 ab.
# 3. Gib das neue Ergebnis mit print() aus.
# 4. Gib den Datentyp des Ergebnisses mit print(type(...)) aus.
# ------------------------------------------------------------------------------

speicher_str = "45.8"

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 3: Benutzer-Guthaben
# Ein Nutzer hat ein Startguthaben von 100.00 Euro als Text hinterlegt.
# 1. Wandle 'guthaben_str' mit float() in eine Kommazahl um.
# 2. Der Nutzer kauft ein Tool fuer 24.50 Euro. Ziehe 24.50 ab.
# 3. Gib das Restguthaben mit print() aus.
# 4. Gib den Datentyp des Restguthabens mit print(type(...)) aus.
# ------------------------------------------------------------------------------

guthaben_str = "100.00"

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 4: Laufzeit eines Skripts berechnen
# Ein Skript hat fuer den ersten Schritt 14.2 Sekunden gebraucht (als Text).
# 1. Wandle 'dauer_str' mit float() in eine Kommazahl um.
# 2. Fuer einen zweiten Schritt kommen noch 5.8 Sekunden hinzu. Addiere 5.8 dazu.
# 3. Gib die Gesamtdauer mit print() aus.
# 4. Gib den Datentyp des Ergebnisses mit print(type(...)) aus.
# ------------------------------------------------------------------------------

dauer_str = "14.2"

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 5: Aktivitaetsstatus umwandeln (Zahl zu bool)
# Datenbanken oder APIs liefern Flags oft als Zahl: 1 (aktiv/ja) oder 0 (inaktiv/nein).
# 1. Wandle 'status_code' mit bool() in einen Wahrheitswert um.
# 2. Gib das Ergebnis mit print() aus (sollte True sein).
# 3. Gib den Datentyp des Ergebnisses mit print(type(...)) aus.
# ------------------------------------------------------------------------------

status_code = 1

# Hier deinen Code schreiben:



print("-" * 60)


# AUFGABE 6: Eingabe-Pruefung / Truthiness (Text zu bool)
# In Python wird ein leerer Text ("") zu False, jeder Text mit Inhalt zu True.
# 1. Wandle 'benutzername' mit bool() um (prueft: Wurde etwas eingetippt?).
# 2. Gib das Ergebnis mit print() aus (sollte True sein).
# 3. Gib den Datentyp des Ergebnisses mit print(type(...)) aus.
# (Hinweis: Ein leerer String "" wuerde False ergeben!)
# ------------------------------------------------------------------------------

benutzername = "Admin_Luise"

# Hier deinen Code schreiben:



print("=" * 60)

